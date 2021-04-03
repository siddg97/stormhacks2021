from constants import WAV_EXT, WEBM_EXT
import subprocess
import os
from google.cloud import speech, storage

def delete_local_file(file_path):
    os.remove(file_path)

def convert_to_wav(file):
    """
    Convert webm encoded file to wav audio encoding
    """
    command = ['ffmpeg', '-i', f'{file}{WEBM_EXT}', f'{file}{WAV_EXT}', '-loglevel', 'error']
    subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)

def read_file(bucket_name, blob, destination):
    """
    Fetch the file from google cloud storage bucket

    @param: bucket_name - Name of google cloud storage bucket
    @param: blob        - Name of blob to be downloaded from GCS bucket
    @param: destination - Path to which blob from GCS will be downloaded to
    """
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob)
    blob.download_to_filename(destination)

def upload_file(bucket_name, blob, destination):
    """
    Upload the file to google cloud storage bucket

    @param: bucket_name - Name of google cloud storage bucket
    @param: blob        - Name of blob to be uploaded to GCS bucket
    @param: destination - Path to where the blob will be uploaded to GCS bucket
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob)
    blob.upload_from_filename(destination)

def get_transcript(uri):
    """
    Get transcript for a audio WAVE file stored in GCS bucket

    @param: uri - File location in the google cloud storage bucket
    """
    # create speech client
    client = speech.SpeechClient()

    # actual audio file to recognize
    audio = speech.RecognitionAudio(uri=uri)
    # recognition config
    config = speech.RecognitionConfig(
        language_code="en-US",
        audio_channel_count=1
    )

    # execute the recognition API
    operation = client.long_running_recognize(config=config, audio=audio)
    print("Waiting for operation to complete...")
    # wait for 90 seconds max
    response = operation.result(timeout=90)

    transcript = ""
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        transcript = transcript + result.alternatives[0].transcript
    return transcript