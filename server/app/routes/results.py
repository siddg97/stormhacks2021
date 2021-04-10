from app.utils.cookies import get_user_cookie
from app.errors import ForbiddenError, NotFoundError
from app.mongodb.queries import (
    get_question_by_id,
    get_questions_for_user,
)
from app.utils.cookies import get_user_cookie


def result_routes(app):
    @app.route("/api/questions/<question_id>/results", methods=["GET"])
    def get_results_question(question_id):
        user_id = get_user_cookie()
        if not user_id:
            app.logger.warning(
                "Revoked unauthorized access to question[%s]", question_id
            )
            raise ForbiddenError()

        question = get_question_by_id(question_id)
        if not question:
            raise NotFoundError()

        if question["user_id"] != user_id:
            app.logger.warning(
                "Revoked unauthorized access to question[%s] by user[%s]",
                question_id,
                user_id,
            )
            raise ForbiddenError()
        return {"result": question["stats"]}, 200

    @app.route("/api/questions/results", methods=["GET"])
    def get_results_user():
        user_id = get_user_cookie()
        if not user_id:
            raise ForbiddenError()

        user_questions = get_questions_for_user(user_id)
        if not user_questions:
            raise NotFoundError()

        aggd = []
        for q in user_questions:
            stats = q["stats"]
            aggd.append(stats)

        num_pauses = 0
        wpm = 0
        for each in aggd:
            num_pauses += int(each["number_of_pauses"])
            wpm += int(each["words_per_min"])

        return {
            "results": {
                "words_per_minute": {"total": wpm, "avg": wpm / len(aggd)},
                "number_of_pauses": {
                    "total": num_pauses,
                    "avg": num_pauses / len(aggd),
                },
            },
        }
