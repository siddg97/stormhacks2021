import os
from bson import ObjectId
from pymongo import MongoClient

from app.mongodb.queries import write_stats


mongo = MongoClient(os.getenv("TEST_MONGO_URI"))
db = mongo["test_db"]


def drop_all_collections():
    """
    Drop all collections in mongodb instance
    """
    db.users.drop()
    db.questions.drop()


def find_question_by_id(question_id):
    """
    Retrieve a particular question document

    @param: question_id - id for the question to be retrieved
    """
    return db.questions.find_one({"_id": ObjectId(question_id)})


def insert_question(question):
    """
    Insert a particular question

    @param: question - JSON object containing question data to be inserted
    """
    return db.questions.insert_one(question)


def write_test_stats(question):
    """
    Update a particular question document's stats
    
    @param: question - JSON object containing question data to be updated
    """
    return write_stats(question["_id"], question["stats"])