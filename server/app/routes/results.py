from app.utils.cookies import get_user_cookie
from app.errors import ForbiddenError, NotFoundError
from app.mongodb.queries import get_questions_for_user


def result_routes(app):
    @app.route("/api/results/<question_id>", methods=["GET"])
    def get_results(uid, type):
        """
        - files dir in = <uid>
        - file names in user doc under bucket_files key
        - fetch files, analyse audio
        - aggregate stats
        - return aggd and individual stats
        """
        user_id = get_user_cookie()
        if not user_id:
            raise ForbiddenError()

        user_questions = get_questions_for_user(user_id)
        if not user_questions:
            raise NotFoundError()
        # bucket_dir = uid
        # all_stats = []

        # for each in user["bucket_files"]:
        #     file_path = f"{bucket_dir}/{each}"
        #     transcript = get_transcript(f"gs://{GCS_BUCKET}/{file_path}")
        #     stats = get_stats(transcript, each, TMP_DIR)
        #     all_stats.append(stats)

        # num_pauses = 0
        # en = 72 if type == "bad" else 80
        # wpm = 0
        # for each in all_stats:
        #     num_pauses += int(each["number_of_pauses"])
        #     wpm += int(each["words_per_min"])

        # return {
        #     "stats": {
        #         "wpm": {"total": wpm, "avg": wpm / len(all_stats)},
        #         "np": {"total": num_pauses, "avg": num_pauses / len(all_stats)},
        #         "en": en,
        #     },
        # }

    return app
