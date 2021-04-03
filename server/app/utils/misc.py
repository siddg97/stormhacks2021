import os
from datetime import datetime


def delete_local_file(file_path):
    os.remove(file_path)


def now():
    return datetime.utcnow().isoformat()
