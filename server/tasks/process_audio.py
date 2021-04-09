from app.utils.constants import TMP_DIR, WAV_EXT
from app.utils.gcs import decompose_gcs_uri
from app.utils.audio import compute_stats
from app.utils.misc import delete_local_file
from tasks import celery
from tasks.db import Mongo


def metadata(message, current, result=None, total=100):
    data = {"current": current, "total": total, "status": message}
    if result != None:
        data["result"] = result
    return data


@celery.task(bind=True)
def process_audio_stats(self, file_uri):
    _, _, file = decompose_gcs_uri(file_uri)
    question_id = file.split(".")[0]

    self.update_state(state="PROGRESS", meta=metadata("Computing stats", 20))
    print("Computing stats...")
    stats = compute_stats(file_uri)

    self.update_state(state="PROGRESS", meta=metadata("Uploading stats", 80))
    print("saving stats...")
    mongo = Mongo()
    mongo.save_stats(question_id, stats)

    self.update_state(state="PROGRESS", meta=metadata("Cleaning up", 90))
    print("Cleaning up...")
    delete_local_file(f"{TMP_DIR}/{question_id}.TextGrid")
    delete_local_file(f"{TMP_DIR}/{question_id}{WAV_EXT}")

    return metadata("Completed processing stats!", 100, stats)
