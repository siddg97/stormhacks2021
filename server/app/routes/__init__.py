from app.routes.answer import answer_routes
from app.routes.questions import question_routes


def register_routes(app):
    app = question_routes(app)
    app = answer_routes(app)
    return app