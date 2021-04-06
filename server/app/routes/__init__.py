from app.routes.answer import answer_routes
from app.routes.questions import question_routes


def register_routes(app):
    @app.route("/api/ping", methods=["GET"])
    def ping():
        app.logger.info("Server was pinged and it ponged")
        return {"ping": "pong"}, 200

    app = question_routes(app)
    app = answer_routes(app)
    return app