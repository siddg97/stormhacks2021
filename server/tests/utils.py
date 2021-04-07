from bson import ObjectId
from pymongo import MongoClient
import os

from app.factory import create_flask
from app.mongodb.queries import create_question
from app.mongodb.utils import serialize_id
from app.utils.constants import USER_COOKIE_KEY

mongo = MongoClient(os.getenv("TEST_MONGO_URI"))
db = mongo["test_db"]


def drop_all_collections():
    db.users.drop()
    db.questions.drop()


def get_test_app():
    app = create_flask(True)
    client = app.test_client()
    return client


def set_test_cookie(app, uid=None):
    if not uid:
        gen_uid = new_id()
        app.set_cookie("/", USER_COOKIE_KEY, gen_uid)
        return gen_uid

    app.set_cookie("/", USER_COOKIE_KEY, uid)
    return uid


def new_id():
    return str(ObjectId())


def find_question_by_id(question_id):
    return db.questions.find_one({"_id": ObjectId(question_id)})


def build_question(description, uid):
    question = create_question(description, uid)
    question_doc = db.questions.insert_one(question)
    question["_id"] = serialize_id(question_doc.inserted_id)
    return question


def build_questions(uid, n=5):
    questions = [None] * n
    for i in range(n):
        questions[i] = build_question(f"Question {i+1}", uid)
    return questions