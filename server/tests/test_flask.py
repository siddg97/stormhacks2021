import pytest
from app import create_app
from bson import ObjectId

from tests.utils import find_question_in_db


@pytest.fixture
def client():
    app = create_app(True)
    return app.test_client()


def test_ping_pong(client):
    """GET /api/ping returns 200"""
    res = client.get("/api/ping")

    assert res.status_code == 200
    assert res.json == {"ping": "pong"}


def test_add_questions_and_get_user_id_in_cookie(client):
    """POST /api/questions sets cookie if not user found"""
    res = client.post("/api/questions", json=dict(questions=["question 1"]))

    assert res.status_code == 200
    assert "IB_USER_ID" in res.headers["Set-Cookie"]
    assert len(res.json["questions"]) == 1


def test_get_question_by_id(client):
    res = client.get(f"/api/questions/{str(ObjectId())}")
    assert res.status_code == 404

    res = client.post("/api/questions", json=dict(questions=["question 1"]))
    assert res.status_code == 200
    assert len(res.json["questions"]) == 1
    qid = res.json["questions"][0]

    res = client.get(f"/api/questions/{qid}")
    assert res.status_code == 200
    question = res.json.get("question")
    assert question

    question_doc = find_question_in_db(question["_id"])
    assert question_doc
    assert question_doc["description"] == "question 1"
