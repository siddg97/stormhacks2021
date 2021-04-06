from app.mongodb.db import init_mongo
from flask import Flask

import os

from app.routes import register_routes


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
        return {"ping": "pong"}, 200

    app = register_routes(app)

    return app


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
