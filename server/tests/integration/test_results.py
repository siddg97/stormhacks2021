import pytest
from bson import ObjectId
from tests.utils import (
    get_test_app, 
    drop_all_collections, 
    set_test_cookie,
    build_question
)


@pytest.fixture
def app():
    app = get_test_app()
    yield app
    drop_all_collections()


#########################################################
## GET /api/questions/<question_id>/results Test Cases ##
#########################################################


class TestGetResultsByQuestionId:
    def test_get_results_401(self, app):
        """
        GET /api/questions/<question_id>/results: accessing endpoint without valid user cookie
        """
        res = app.get(f"/api/questions/{str(ObjectId())}/results")
        assert res.status_code == 401

    def test_get_results_404(self, app):
        """
        GET /api/questions/<question_id>/results: provide invalid question_id
        """
        uid = str(ObjectId())
        set_test_cookie(app, uid)

        res = app.get(f"/api/questions/{str(ObjectId())}/results")
        assert res.status_code == 404

    def test_get_results_201(self, app):
        """
        GET /api/questions/<question_id>/results:
        """
        uid = str(ObjectId())
        set_test_cookie(app, uid)
        question_id = build_question("Question 1", uid)["_id"]

        res = app.get(f"/api/questions/{question_id}/results")
        print(res.json)
        assert res.status_code == 200
        assert res.json.get("result")
        assert len(res.json.get("result")) >= 1

    def test_get_results_incorrect_uid(self, app):
        """
        GET /api/questions/<question_id>/results: attempt to retrieve question with invalid uid
        """
        uid_one = str(ObjectId())
        set_test_cookie(app, uid_one)
        question_one_id = build_question("Question 1", uid_one)["_id"]

        uid_two = str(ObjectId())
        set_test_cookie(app, uid_two)
        question_two_id = build_question("Question 2", uid_two)["_id"]

        res = app.get(f"/api/questions/{question_one_id}/results")
        assert res.status_code == 401

        res = app.get(f"/api/questions/{question_two_id}/results")
        assert res.status_code == 200

