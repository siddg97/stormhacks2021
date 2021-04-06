from app.mongodb.queries import (
    bulk_create_questions,
    create_new_user,
    create_question,
    get_question_by_id,
    get_questions_for_user,
)
from app.utils.cookies import get_user_cookie, set_user_cookie

from flask.ctx import after_this_request
from flask import request


def question_routes(app):
    @app.route("/api/questions", methods=["POST"])
    def save_questions():
        """
        POST /api/questions

        Submit up to five questions at a time. Identifies user via cookie
        in the request else creates new user id and sends cookie in response
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
        """
        GET /api/questions/<question_id>
        Fetch information about a specific question matching question_id, else return a 404
        """
        question = get_question_by_id(question_id)
        return {"question": question}, 404 if not question else 200

    @app.route("/api/questions", methods=["GET"])
    def get_user_questions():
        """
        GET /api/questions
        Fetch questions for the current user if cookie is found, else return a 404
        """
        user_id = get_user_cookie()
        # TODO handle 404 case
        questions = get_questions_for_user(user_id)
        # TODO handle 404 case
        return {"questions": questions}

    return app