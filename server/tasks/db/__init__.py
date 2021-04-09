from bson.objectid import ObjectId
from pymongo import MongoClient

from tasks.db.config import MONGO_URI


class Mongo:
    def __init__(self):
        self.conn = MongoClient(MONGO_URI, connect=False)

    def save_stats(self, question_id, stats):
        """
        Save computed stats for a question to db
        """
        self.conn["db"]["questions"].find_one_and_update(
            {"_id": ObjectId(question_id)}, {"$set": {"stats": stats}}
        )