from bson import ObjectId

from app.mongodb.queries import create_question
from app.mongodb.utils import serialize_id

from tests.utils.test_db import ( 
    insert_question, 
    write_test_stats
)


def new_id():
    """
    Generates new bson ObjectId
    """
    return str(ObjectId())


def build_question(description, uid):
    """
    Builds JSON structure for a single question and inserts to db

    @param: description - string for question description
    @param: uid         - id for user submitting the question
    """
    question = create_question(description, uid)
    question_doc = insert_question(question)
    question["_id"] = serialize_id(question_doc.inserted_id)
    return question


def build_questions(uid, n=5):
    """
    Builds JSON structure for n questions and inserts them to db

    @param: uid - id for user submitting the questions
    @param: n   - number of questions generated
    """
    questions = [None] * n
    for i in range(n):
        questions[i] = build_question(f"Question {i+1}", uid)
    return questions

def seed_questions_with_sample_results(questions, n=10):
    """
    Seeds an array of questions with sample results, each incremented by n
    
    @param: questions - array of questions being seeded with data
    @param: n         - value to increment results stats by
    """
    for q in questions:
        q["stats"]["number_of_pauses"] += n
        q["stats"]["words_per_min"] += n
        write_test_stats(q)
    return questions

