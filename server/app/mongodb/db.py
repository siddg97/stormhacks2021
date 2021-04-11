from flask_pymongo import PyMongo

mongo = PyMongo()


def init_mongo(app):
    # Get mongo config from flask app
    MONGO_URI = app.config["MONGO_URI"]
    TIMEOUT = app.config["MONGO_TIMEOUT"]

    mongo.init_app(
        app,
        uri=MONGO_URI,
        connect=False,
        connectTimeoutMS=TIMEOUT,
        serverSelectionTimeoutMS=TIMEOUT,
        socketTimeoutMS=TIMEOUT,
    )
