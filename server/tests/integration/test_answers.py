import pytest
import io
import os
from bson import ObjectId

from app.utils.constants import TMP_DIR, WAV_EXT, WEBM_EXT

from tests.utils.test_gcs import get_test_blob_url
from tests.utils.test_db import drop_all_collections
from tests.utils.test_factory import (
    new_id,
    build_question
)
from tests.utils.test_app import (
    get_test_app, 
    set_test_cookie
)
from tests.utils.test_audio import (
    generate_sample_webm,
    cleanup_webm,
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
        uid = set_test_cookie(app)

        file = dict(audio=(io.BytesIO(str.encode(uid)), "test.txt"))
        res = app.post(
            f"/api/questions/{new_id()}/answer",
            data=file,
            content_type="multipart/form-data",
        )
        assert res.status_code == 400

    def test_submit_answer_401(self, app):
        """
        POST /api/questions/<question_id>/answer: accessing endpoint without user permission
        """
        res = app.post(f"/api/questions/{new_id()}/answer")
        assert res.status_code == 401

    def test_submit_answer_201(self, app):
        """
        POST /api/questions/<question_id>/answer: submit proper file and check local directories
        """
        uid = set_test_cookie(app)
        question_id = build_question("test question", uid)["_id"]

        webm_path = f"{TMP_DIR}/{question_id}{WEBM_EXT}"
        webm = generate_sample_webm(question_id)
        assert webm
        assert os.path.exists(webm_path)

        res = app.post(
            f"/api/questions/{question_id}/answer",
            data=dict(audio=webm),
            content_type="multipart/form-data",
        )
        assert res.status_code == 201

        question_response = res.json.get("question")
        assert question_response
        assert len(question_response) >= 1

        blob_path = f"{uid}/{question_id}{WEBM_EXT}"
        blob_url = res.json.get("question").get("answer")
        assert blob_url
        assert blob_url == get_test_blob_url(blob_path)

        cleanup_webm(uid, question_id)
        assert os.path.exists(webm_path) is False