from app.routes.answer import answer_routes
from app.routes.questions import question_routes
import tasks


def register_routes(app):
    @app.route("/api/ping", methods=["GET"])
    def ping():
        app.logger.info("Server was pinged and it ponged")
        return {"ping": "pong"}, 200

    @app.route("/api/test", methods=["GET"])
    def testt():
        task_ids = [None] * 10
        for i in range(10):
            tid = tasks.add.delay(i, 5)
            task_ids[i] = tid.id
            app.logger.info("Task[%s] started", tid)
        return {"tasks": task_ids}, 200

    app = question_routes(app)
    app = answer_routes(app)
    return app