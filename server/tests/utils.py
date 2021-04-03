from bson import ObjectId
from pymongo import MongoClient
import os

mongo = MongoClient(os.getenv("TEST_MONGO_URI"))
db = mongo["test_db"]


def find_question_in_db(question_id):
    return db.questions.find_one({"_id": ObjectId(question_id)})