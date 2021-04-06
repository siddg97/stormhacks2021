import pytest
from tests.utils import get_test_app


@pytest.fixture
def app():
    app = get_test_app()
    return app


def test_ping_pong(app):
    """GET /api/ping returns 200"""
    res = app.get("/api/ping")

    assert res.status_code == 200
    assert res.json == {"ping": "pong"}
