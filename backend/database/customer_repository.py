# backend/database/mongo_connection.py

from pymongo import MongoClient
from backend.utils.config import MONGO_URI, DATABASE_NAME


class MongoConnection:
    """
    MongoDB Connection Manager
    """

    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]

    def get_database(self):
        return self.db


# Create global connection instance
mongo_connection = MongoConnection()


def get_database():
    """
    Return database instance
    """
    return mongo_connection.get_database()
