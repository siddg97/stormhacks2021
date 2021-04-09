from app.utils.constants import TMP_DIR, WAV_EXT
from app.utils.gcs import decompose_gcs_uri
from app.utils.audio import compute_stats
from app.utils.misc import delete_local_file
from tasks import celery
from tasks.db import Mongo


@celery.task(bind=True)
def process_audio_stats(self, file_uri):
    _, _, file = decompose_gcs_uri(file_uri)
    question_id = file.split(".")[0]
    print("Computing stats...")
    stats = compute_stats(file_uri)
    print("saving stats...")
    mongo = Mongo()
    mongo.save_stats(question_id, stats)
    print("Clening up...")
    delete_local_file(f"{TMP_DIR}/{question_id}.TextGrid")
    delete_local_file(f"{TMP_DIR}/{question_id}{WAV_EXT}")
