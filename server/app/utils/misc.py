import os
from datetime import datetime


def delete_local_file(file_path):
    os.remove(file_path)


def now():
    return datetime.utcnow().isoformat()


def find(pred, iterable):
    for element in iterable:
        if pred(element):
            return element
    return None
