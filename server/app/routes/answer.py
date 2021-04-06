from app.errors import BadRequestError, ForbiddenError
from app.mongodb.queries import (
    add_answer,
)
from app.utils.cookies import get_user_cookie
from app.utils.misc import delete_local_file
from app.utils.gcs import get_blob_url, upload_file
from app.utils.audio import convert_to_wav
from app.utils.constants import GCS_BUCKET, TMP_DIR, WEBM_EXT, WAV_EXT

from flask import request


def answer_routes(app):
    @app.route("/api/questions/<question_id>/answer", methods=["POST"])
    def submit_answer(question_id):
        """
        1. Extract webm audio file and convert to wav file
        2. Upload to a the users folder in cloud storage with name as question id
        """
        user_id = get_user_cookie()
        if not user_id:
            raise ForbiddenError()

        # Extract file and sanity check
        webm_file = request.files["audio"]
        if webm_file.filename.split(".")[1] != "webm":
            raise BadRequestError()

        # Save webm file to convert
        blob_name = question_id
        file_path = f"{TMP_DIR}/{blob_name}"
        wav_file_path = f"{file_path}{WAV_EXT}"
        webm_file_path = f"{file_path}{WEBM_EXT}"
        gcs_path = f"{user_id}/{blob_name}{WAV_EXT}"

        app.logger.info(
            "Saving answer .webm for question[%s] by user[%s]", question_id, user_id
        )
        webm_file.save(webm_file_path)

        # convert webm file to wav
        convert_to_wav(file_path)
        app.logger.info(
            "Coverting answer .webm for question[%s] by user[%s] to .wav file",
            question_id,
            user_id,
        )

        # upload to bucket
        upload_file(GCS_BUCKET, gcs_path, wav_file_path)
        app.logger.info(
            "Uploaded answer .wav for question[%s] by user[%s] to %s",
            question_id,
            user_id,
            get_blob_url(GCS_BUCKET, gcs_path),
        )

        # add file path to question doc in db
        question = add_answer(question_id, gcs_path)

        # cleanup webm and wav file in temp directory
        delete_local_file(webm_file_path)
        delete_local_file(wav_file_path)
        app.logger.info(
            "Cleaned up temp answer files for question[%s] by user[%s]",
            question_id,
            user_id,
        )

        return {"question": question}, 201

    return app