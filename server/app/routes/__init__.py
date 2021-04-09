from app.routes.answer import answer_routes
from app.routes.questions import question_routes
from app.routes.results import result_routes
import tasks


def register_routes(app):
    @app.route("/api/ping", methods=["GET"])
    def ping():
        app.logger.info("Server was pinged and it ponged")
        return {"ping": "pong"}, 204

    @app.route("/api/test", methods=["GET"])
    def test_task():
        task_ids = [None] * 10
        for i in range(10):
            tid = tasks.add.delay(i, 5)
            task_ids[i] = tid.id
            app.logger.info("Task[%s] started", tid)
        return {"tasks": task_ids}, 200

    question_routes(app)
    answer_routes(app)
    result_routes(app)