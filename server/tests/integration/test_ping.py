import pytest

from tests.utils.test_app import get_test_app
from tests.utils.test_db import drop_all_collections

@pytest.fixture
def app():
    app = get_test_app()
    yield app
    drop_all_collections()


def test_ping_pong(app):
    """GET /api/ping returns 200"""
    res = app.get("/api/ping")
    assert res.status_code == 200
    assert res.json.get("ping") == "pong"
