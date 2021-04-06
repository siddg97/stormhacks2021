from app.mongodb.queries import (
    add_answer,
)
from app.utils.cookies import get_user_cookie
from app.utils.misc import delete_local_file
from app.utils.gcs import upload_file
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
        # Extract file and sanity check
        webm_file = request.files["audio"]
        if webm_file.filename.split(".")[1] != "webm":
            return {"error": "Invalid file type detected"}, 400

        # Save webm file to convert
        blob_name = question_id
        file_path = f"{TMP_DIR}/{blob_name}"
        wav_file_path = f"{file_path}{WAV_EXT}"
        webm_file_path = f"{file_path}{WEBM_EXT}"
        gcs_path = f"{user_id}/{blob_name}{WAV_EXT}"

        print("[INFO]: Saving .webm file")
        webm_file.save(webm_file_path)

        # convert webm file to wav
        convert_to_wav(file_path)
        print("[INFO]: Converting .webm to .wav file")

        # upload to bucket
        upload_file(GCS_BUCKET, gcs_path, wav_file_path)
        print("[INFO]: Uploaded .wav file to GCS bucket")

        # add file path to question doc in db
        question = add_answer(question_id, gcs_path)

        # cleanup webm and wav file in temp directory
        print("[INFO]: Cleaning up local temp directory")
        delete_local_file(webm_file_path)
        delete_local_file(wav_file_path)
        print("[INFO]: Cleanup complete !!")
        return {"question": question}, 201

    return app