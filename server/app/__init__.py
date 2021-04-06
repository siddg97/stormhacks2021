from app.errors.handlers import register_error_handlers
from app.mongodb.db import init_mongo
from app.routes import register_routes
from flask import Flask
import os
from logging.config import dictConfig

# logging config
dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)


def create_app(test=False):
    app = Flask(__name__)

    if test:
        app.config["TESTING"] = True
        app.config["MONGO_URI"] = os.getenv("TEST_MONGO_URI")
    else:
        app.config["MONGO_URI"] = os.getenv("MONGO_URI")

    init_mongo(app)
    app = register_error_handlers(app)
    app = register_routes(app)

    return app