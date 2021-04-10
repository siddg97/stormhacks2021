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


def info_log(message, question_id):
    print(f"[INFO]: {message} for question[{question_id}]")


@celery.task(bind=True)
def process_audio_stats(self, file_uri):
    _, _, file = decompose_gcs_uri(file_uri)
    question_id = file.split(".")[0]

    self.update_state(state="PROGRESS", meta=metadata("Processing audio", 40))
    info_log("Processing audio", question_id)
    stats = compute_stats(file_uri)

    self.update_state(state="PROGRESS", meta=metadata("Uploading stats", 80))
    info_log(f"Saving result", question_id)
    mongo = Mongo()
    mongo.save_stats(question_id, stats)

    self.update_state(state="PROGRESS", meta=metadata("Cleaning up", 90))
    info_log("Cleaning up temp files", question_id)
    delete_local_file(f"{TMP_DIR}/{question_id}.TextGrid")
    delete_local_file(f"{TMP_DIR}/{question_id}{WAV_EXT}")

    info_log("Processing audio complete", question_id)

    return metadata("Completed processing stats!", 100, stats)
