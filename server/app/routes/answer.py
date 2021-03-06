from app.errors import BadRequestError
from app.mongodb.queries import (
    add_answer,
)
from app.utils.cookies import get_user_cookie
from app.utils.misc import delete_local_file
from app.utils.gcs import get_blob_url, upload_file
from app.utils.audio import convert_to_wav
from app.utils.constants import GCS_BUCKET, TMP_DIR, WEBM_EXT, WAV_EXT

from flask import request, url_for

from tasks.process_audio import process_audio_stats


def answer_routes(app):
    @app.route("/api/questions/<question_id>/answer", methods=["POST"])
    def submit_answer(question_id):
        """
        1. Extract webm audio file and convert to wav file
        2. Upload to a the users folder in cloud storage with name as question id
        """
        user_id = get_user_cookie(True)

        # Extract file and sanity check
        webm_file = request.files["audio"]
        if webm_file.filename.split(".")[1] != "webm":
            raise BadRequestError()

        blob_name = question_id
        gcs_file_path = f"{user_id}/{blob_name}{WEBM_EXT}"
        local_file_path = f"{TMP_DIR}/{blob_name}"
        webm_file_path = f"{local_file_path}{WEBM_EXT}"

        app.logger.info(
            "Saving answer .webm for question[%s] by user[%s]", question_id, user_id
        )
        webm_file.save(webm_file_path)

        # upload to bucket
        app.logger.info(
            "Uploading answer .webm for question[%s] by user[%s] to %s",
            question_id,
            user_id,
            get_blob_url(GCS_BUCKET, gcs_file_path),
        )
        upload_file(GCS_BUCKET, gcs_file_path, webm_file_path)

        # add file path to question doc in db
        question = add_answer(question_id, gcs_file_path)

        # Trigger task and obtain task id
        process_task = process_audio_stats.delay(question["answer"])
        task_id = process_task.id
        app.logger.info("Triggered processing stats task[%s]", task_id)

        # cleanup webm and wav file in temp directory
        delete_local_file(webm_file_path)
        # delete_local_file(wav_file_path)
        app.logger.info(
            "Cleaned up temp answer files for question[%s] by user[%s]",
            question_id,
            user_id,
        )

        return {
            "question": question,
            "task_id": task_id,
            "poll_url": url_for("get_task_status", task_id=task_id),
        }, 201
