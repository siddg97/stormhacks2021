import pytest
import io
from bson import ObjectId
from tests.utils import (
    get_test_app,
    drop_all_collections,
    set_test_cookie,
    build_question,
    generate_sample_webm,
    cleanup_webm
)

@pytest.fixture
def app():
    app = get_test_app()
    yield app
    drop_all_collections()


#########################################################
## POST /api/questions/<question_id>/answer Test Cases ##
#########################################################


class TestSubmitAnswer:
    def test_submit_answer_400(self, app):
        """
        POST /api/questions/<question_id>/answer: uses malformed file ending
        """
        uid = str(ObjectId())
        set_test_cookie(app, uid)

        file = dict(audio=(io.BytesIO(str.encode(uid)), 'test.txt'))
        res = app.post(f"/api/questions/{str(ObjectId())}/answer", data=file, content_type='multipart/form-data')
        assert res.status_code == 400
    
    def test_submit_answer_401(self, app):
        """
        POST /api/questions/<question_id>/answer: accessing endpoint without user permission
        """
        res = app.post(f"/api/questions/{str(ObjectId())}/answer")
        assert res.status_code == 401

    def test_submit_answer_201(self, app):
        """
        POST /api/questions/<question_id>/answer: submit proper file and check local directories
        """
        uid = str(ObjectId())
        set_test_cookie(app, uid)
        question = build_question("test question", uid)["_id"]

        webm = generate_sample_webm(question)
        
        res = app.post(f"/api/questions/{question}/answer", data=dict(audio=webm), content_type='multipart/form-data')
        assert res.status_code == 201

        cleanup_webm(question)