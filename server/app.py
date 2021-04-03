from mongodb.db import init_mongo
from mongodb.queries import (
    add_answer,
    bulk_create_questions,
    create_new_user,
    create_question,
    get_question_by_id,
)
from utils.cookies import get_user_cookie, set_user_cookie

from utils.misc import delete_local_file, now
from utils.gcs import upload_file
from utils.audio import convert_to_wav
from utils.constants import GCS_BUCKET, TMP_DIR, USER_COOKIE_KEY, WEBM_EXT, WAV_EXT

from flask.ctx import after_this_request
from flask import Flask, request

import os


def create_app(test=False):
    app = Flask(__name__)

    if test:
        app.config["TESTING"] = True
        app.config["MONGO_URI"] = os.getenv("TEST_MONGO_URI")
    else:
        app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    init_mongo(app)

    @app.route("/api/ping", methods=["GET"])
    def ping():
        return {"pong": "pong"}, 200

    @app.route("/api/questions", methods=["POST"])
    def index():
        """
        1. Check for user_id in cookie, if present get user else create new user
        2. Create new question doc and mark with user id from previous step
        """
        user_id = get_user_cookie()
        if not user_id:
            user_id = create_new_user()
            after_this_request(set_user_cookie(user_id))

        body = request.get_json(force=True)
        questions = body["questions"]
        questions = list(map(lambda desc: create_question(desc, user_id), questions))
        question_ids = bulk_create_questions(questions)

        return {"questions": question_ids}, 200

    @app.route("/api/questions/<question_id>", methods=["GET"])
    def get_question(question_id):
        question = get_question_by_id(question_id)
        return {"question": question}, 200

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
        return {"question": question}, 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0")


# @app.route('/api/results/<uid>/<type>', methods=['GET'])
# def get_results(uid, type):
#     """
#     - files dir in = <uid>
#     - file names in user doc under bucket_files key
#     - fetch files, analyse audio
#     - aggregate stats
#     - return aggd and individual stats
#     """
#     user = users.find_one({ 'uid': uid })
#     bucket_dir = uid
#     all_stats = []

#     for each in user['bucket_files']:
#         file_path = f"{bucket_dir}/{each}"
#         transcript = get_transcript(f'gs://{GCS_BUCKET}/{file_path}')
#         stats = get_stats(transcript, each, TMP_DIR)
#         all_stats.append(stats)

#     num_pauses = 0
#     en = 72 if type == 'bad' else 80
#     wpm = 0
#     for each in all_stats:
#         num_pauses+= int(each['number_of_pauses'])
#         wpm += int(each['words_per_min'])

#     return {
#         'stats': {
#             'wpm': {
#                 'total': wpm,
#                 'avg': wpm /len(all_stats)
#             },
#             'np': {
#                 'total': num_pauses,
#                 'avg': num_pauses /len(all_stats)
#             },
#             'en': en,
#         },
#     }
