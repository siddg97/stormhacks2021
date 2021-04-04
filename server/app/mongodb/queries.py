from datetime import datetime

from bson.objectid import ObjectId
from pymongo import ReturnDocument

from app.mongodb.db import mongo
from app.mongodb.utils import serialize_doc, serialize_id
from app.utils.constants import GCS_BUCKET


def create_new_user():
    """
    Creates a new user in db with empty questions array and creation date

    @returns:  user_id - mongodb user document ID
    """
    user = {"createdOn": datetime.utcnow().isoformat()}
    user_doc = mongo.db.users.insert_one(user)
    return serialize_id(user_doc.inserted_id)


def get_user_by_id(user_id):
    """
    Get a user document from db if user_id is valid

    @param: user_id - _id for the corresponding user to get
    @returns: user doc as python dict if valid user_id, else None
    """
    user = mongo.db.users.find_one(ObjectId(user_id))
    return serialize_doc(user)


def bulk_create_questions(questions):
    """
    Bulk write a list of question dicts

    @param: questions - list of question dicts
    @returns: list of question ids
    """
    result = mongo.db.questions.insert_many(questions)
    return list(map(serialize_id, result.inserted_ids))


def create_question(description, user_id):
    """
    Creates a new question dict

    @params: description    - question body test
    @params: user_id        - user id associated to the question
    @returns: python dict representing the question doc in db
    """
    return {
        "description": description,
        "user_id": user_id,
        "stats": {
            "words_per_min": 0,
            "filler_words_per_min": 0,
            "enunciation_percent": 0,
        },
        "answer": "",
    }


def get_question_by_id(question_id):
    """
    Get a question document from db if question_id is valid

    @param: question_id - _id for the corresponding question to get
    @returns: question doc as python dict if valid question_id, else None
    """
    question = mongo.db.questions.find_one(ObjectId(question_id))
    return serialize_doc(question)


def add_answer(question_id, answer_file_path):
    selector = {"_id": ObjectId(question_id)}
    updated_question = mongo.db.questions.find_one_and_update(
        selector,
        {"$set": {"answer": f"gs://{GCS_BUCKET}/{answer_file_path}"}},
        return_document=ReturnDocument.AFTER,
    )
    return serialize_doc(updated_question)
