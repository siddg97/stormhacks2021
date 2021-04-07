import pytest
import json
from unittest.mock import patch, call
from tasks import add
from tests.utils import drop_all_collections, get_test_app


@pytest.fixture
def app():
    app = get_test_app()
    yield app
    drop_all_collections()


class TestAddTask:
    def test_route(self, app):
        res = app.get("/api/test")
        assert res.status_code == 200
        assert res.json
        assert len(res.json["tasks"]) == 10

    @patch("tasks.add.delay")
    def test_mock_task(self, mock_run):
        assert add.delay(1, 1)
        add.delay.assert_called_once_with(1, 1)

        assert add.delay(1, 2)
        assert add.delay.call_count == 2

        assert add.delay(2, 3)
        assert add.delay.call_count == 3
