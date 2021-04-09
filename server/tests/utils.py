from bson import ObjectId
from pymongo import MongoClient
from werkzeug.datastructures import FileStorage
import os
import subprocess

from app.factory import create_flask
from app.mongodb.queries import create_question
from app.mongodb.utils import serialize_id
from app.utils.constants import USER_COOKIE_KEY
from app.utils.gcs import delete_file
from app.utils.constants import GCS_BUCKET, WAV_EXT

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

def generate_sample_webm(question_id):
    """
    Generate a sample webm file from a question id for testing 
    """
    # ffmpeg -f lavfi -i "sine=frequency=1000:duration=5" test.webm
    command = [
        "ffmpeg",
        "-f",
        "lavfi",
        "-i",
        "sine=frequency=1000:duration=5",
        f"{question_id}.webm"
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

    return retrieve_sample_webm(question_id)

def retrieve_sample_webm(question_id):
    file = f"{question_id}.webm"

    webm = FileStorage(
        stream=open(file, "rb"),
        filename=f"{question_id}.webm",
        content_type="video/webm"
    )
    
    return webm

def cleanup_webm(uid, question_id):
    if os.path.exists(f"{question_id}.webm"):
        os.remove(f"{question_id}.webm")

    gcs_path = f"{uid}/{question_id}{WAV_EXT}"
    delete_file(GCS_BUCKET, gcs_path)