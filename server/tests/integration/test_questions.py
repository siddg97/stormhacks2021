import pytest
from bson import ObjectId
from app.utils.misc import find
from tests.utils import (
    build_question,
    build_questions,
    drop_all_collections,
    find_question_by_id,
    get_test_app,
    set_test_cookie,
)


@pytest.fixture
def app():
    app = get_test_app()
    yield app
    drop_all_collections()


####################################
## POST /api/questions Test Cases ##
####################################


class TestAddQuestions:
    def test_add_questions_set_cookie(self, app):
        """
        POST /api/questions: sets cookie if no existing cookie found
        """
        res = app.post("/api/questions", json=dict(questions=["question 1"]))

        assert res.status_code == 201
        assert "IB_USER_ID" in res.headers["Set-Cookie"]
        assert len(res.json["questions"]) == 1

    def test_add_questions_use_cookie(self, app):
        """
        POST /api/questions: uses existing cookie sent with request
        """
        uid = set_test_cookie(app)
        res = app.post("/api/questions", json=dict(questions=["question 1"]))

        assert res.status_code == 201
        assert not res.headers.get("Set-Cookie")
        assert len(res.json["questions"]) == 1

        question = find_question_by_id(res.json["questions"][0])
        assert question
        assert question["user_id"] == uid


#################################################
## GET /api/questions/<question_id> Test Cases ##
#################################################


class TestGetQuestion:
    def test_get_question_401(self, app):
        res = app.get(f"/api/questions/{str(ObjectId())}")
        assert res.status_code == 401

    def test_get_question_404(self, app):
        uid = str(ObjectId())
        set_test_cookie(app, uid)

        res = app.get(f"/api/questions/{str(ObjectId())}")
        assert res.status_code == 404

    def test_get_question_200(self, app):
        uid = str(ObjectId())
        set_test_cookie(app, uid)
        question_doc = build_question("test question", uid)

        res = app.get(f"/api/questions/{question_doc['_id']}")
        assert res.status_code == 200

        question = res.json.get("question")
        assert question

        question_doc = find_question_by_id(question["_id"])
        assert question_doc
        assert question_doc["description"] == question["description"]
        assert question_doc["user_id"] == question["user_id"]


###################################
## GET /api/questions Test Cases ##
###################################


class TestGetQuestions:
    def test_get_questions_401(self, app):
        res = app.get(f"/api/questions")
        assert res.status_code == 401

    def test_get_questions_404(self, app):
        uid = str(ObjectId())
        set_test_cookie(app, uid)

        res = app.get(f"/api/questions")
        assert res.status_code == 404

    def test_get_questions_200(self, app):
        uid = str(ObjectId())
        set_test_cookie(app, uid)

        question_docs = build_questions(uid, 10)

        res = app.get(f"/api/questions")
        assert res.status_code == 200

        questions_response = res.json.get("questions")
        assert len(questions_response) == 10

        for question in questions_response:
            question_doc = find(lambda q: q["_id"] == question["_id"], question_docs)
            assert question_doc
            assert question_doc["created_on"] == question["created_on"]
            assert question_doc["description"] == question["description"]
            assert question_doc["user_id"] == question["user_id"]