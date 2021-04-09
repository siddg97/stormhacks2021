from bson.objectid import ObjectId
from numpy.lib.function_base import select
from pymongo import ReturnDocument

from app.mongodb.db import mongo
from app.mongodb.utils import serialize_doc, serialize_docs, serialize_id, serialize_ids
from app.utils.constants import GCS_BUCKET
from app.utils.gcs import get_blob_url
from app.utils.misc import now


def create_new_user():
    """
    Creates a new user in db with empty questions array and creation date

    @returns:  user_id - mongodb user document ID
    """
    user = {"createdOn": now()}
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
    return serialize_ids(result.inserted_ids)


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
        "created_on": now(),
        "stats": {
            # total number of syllables
            "number_of_syllables": 0,
            # pauses throughout audio file
            "number_of_pauses": 0,
            # syllables/sec (original duration of audio file)
            "rate_of_speech": 0,
            # syllables/sec (speaking duration of audio file)
            "articulation_rate": 0,
            # seconds of audio with speech
            "speaking_duration": 0,
            # Total duration of audio file
            "original_duration": 0,
            # (speaking duration)/(original duration)
            "balance": 0,
            # words/min
            "words_per_min": 0,
            # mood
            "mood": "",
            # gender
            "gender": "",
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


def get_questions_for_user(user_id):
    questions = mongo.db.questions.find({"user_id": user_id})
    return serialize_docs(questions)


def add_answer(question_id, answer_file_path):
    selector = {"_id": ObjectId(question_id)}
    updated_question = mongo.db.questions.find_one_and_update(
        selector,
        {"$set": {"answer": get_blob_url(GCS_BUCKET, answer_file_path)}},
        return_document=ReturnDocument.AFTER,
    )
    return serialize_doc(updated_question)


def write_stats(question_id, stats):
    selector = {"_id": ObjectId(question_id)}

    updated_question = mongo.db.questions.find_one_and_update(
        selector,
        {"$set": {"stats": stats}},
        return_document=ReturnDocument.AFTER,
    )
    return serialize_doc(updated_question)
