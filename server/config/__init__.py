import os


class Config(object):
    DEBUG = False
    TESTING = False
    MONGO_URI = os.getenv("MONGO_URI")
    CELERY_BROKER_URL = os.getenv("REDIS_URI")
    CELERY_RESULT_BACKEND = os.getenv("REDIS_URI")


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
    MONGO_URI = os.getenv("TEST_MONGO_URI")