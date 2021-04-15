import pytest
from bson import ObjectId

from tests.utils.test_db import drop_all_collections
from tests.utils.test_app import get_test_app, set_test_cookie
from tests.utils.test_factory import (
    new_id,
    build_question,
    build_questions,
    seed_questions_with_sample_results
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
        res = app.get(f"/api/questions/{new_id()}/results")
        assert res.status_code == 401

    def test_get_results_404(self, app):
        """
        GET /api/questions/<question_id>/results: provide invalid question_id
        """
        uid = set_test_cookie(app)

        res = app.get(f"/api/questions/{new_id()}/results")
        assert res.status_code == 404

    def test_get_results_200(self, app):
        """
        GET /api/questions/<question_id>/results: retrieve results for a valid [uid:question_id] combination
        """
        uid = set_test_cookie(app)
        question_id = build_question("Question 1", uid)["_id"]

        res = app.get(f"/api/questions/{question_id}/results")
        assert res.status_code == 200
        assert res.json.get("result")
        assert len(res.json.get("result")) >= 1

    def test_get_results_incorrect_uid(self, app):
        """
        GET /api/questions/<question_id>/results: attempt to retrieve question with invalid uid
        """
        uid_one = set_test_cookie(app)
        question_one_id = build_question("Question 1", uid_one)["_id"]

        uid_two = set_test_cookie(app)
        question_two_id = build_question("Question 2", uid_two)["_id"]

        res = app.get(f"/api/questions/{question_one_id}/results")
        assert res.status_code == 401

        res = app.get(f"/api/questions/{question_two_id}/results")
        assert res.status_code == 200


###########################################
## GET /api/questions/results Test Cases ##
###########################################


class TestGetResultsByUserId:
    def test_get_results_uid_401(self, app):
        """
        GET /api/questions/results: accessing endpoint without valid user cookie
        """
        res = app.get(f"/api/questions/results")
        assert res.status_code == 401

    def test_get_results_uid_404(self, app):
        """
        GET /api/questions/results: attempt to retrieve results without valid questions
        """
        uid = set_test_cookie(app)

        res = app.get(f"/api/questions/results")
        assert res.status_code == 404

    def test_get_results_uid_200(self, app):
        """
        GET /api/questions/results: retrieve valid results
        """
        uid = set_test_cookie(app)
        build_question("Question 1", uid)

        res = app.get(f"/api/questions/results")
        assert res.status_code == 200

    def test_get_results_uid_accuracy(self, app):
        """
        GET /api/questions/results: validate accuracy on retrieved results for a particular user
        """
        uid = set_test_cookie(app)
        
        number_of_questions = 10
        questions = build_questions(uid, number_of_questions)

        result_value = 5
        questions = seed_questions_with_sample_results(questions, result_value)

        res = app.get(f"/api/questions/results")
        assert res.status_code == 200

        results = res.json.get("results")
        assert results

        expected_avg = (number_of_questions * result_value) / number_of_questions
        expected_total = number_of_questions * result_value

        number_of_pauses = results.get("number_of_pauses")
        assert number_of_pauses["avg"] == expected_avg
        assert number_of_pauses["total"] == expected_total

        words_per_minute = results.get("words_per_minute")
        assert words_per_minute["avg"] == expected_avg
        assert words_per_minute["total"] == expected_total

