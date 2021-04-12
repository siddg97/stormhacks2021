from werkzeug.datastructures import FileStorage
import os
import subprocess

from app.utils.misc import delete_local_file
from app.utils.gcs import delete_file
from app.utils.constants import ( 
    GCS_BUCKET, 
    TMP_DIR, 
    WAV_EXT, 
    WEBM_EXT 
) 


def generate_sample_webm(question_id):
    """
    Generate a sample webm file for testing

    @param: question_id - ID for the particular question requesting a .webm sample, required for file name and location in GCS bucket
    """
    command = [
        "ffmpeg",
        "-f",
        "lavfi",
        "-i",
        "sine=frequency=1000:duration=5",
        f"{TMP_DIR}/{question_id}{WEBM_EXT}"
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

    return retrieve_sample_webm(question_id)


def retrieve_sample_webm(question_id):
    """
    Retrieve generated webm sample in local directory

    @param: question_id - id for the particular question with a corresponding .webm file in the local directory
    """
    file = f"{TMP_DIR}/{question_id}{WEBM_EXT}"

    webm = FileStorage(
        stream=open(file, "rb"),
        filename=f"{question_id}{WEBM_EXT}",
        content_type="video/webm"
    )
    
    return webm


def cleanup_webm(uid, question_id):
    """
    Remove local .webm file and delete .wav file from GCS bucket

    @param: uid         - id matching a user-specific blob in GCS bucket
    @param: question_id - id for question with a corresponding .webm file in the local directory
    """
    local_path = f"{TMP_DIR}/{question_id}{WEBM_EXT}"
    if os.path.exists(local_path):
        delete_local_file(local_path)

    gcs_path = f"{uid}/{question_id}{WAV_EXT}"
    delete_file(GCS_BUCKET, gcs_path)