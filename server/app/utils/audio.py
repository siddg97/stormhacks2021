from app.utils.constants import WAV_EXT, WEBM_EXT
import subprocess
from google.cloud import speech


def convert_to_wav(file):
    """
    Convert webm encoded file to wav audio encoding
    """
    command = [
        "ffmpeg",
        "-i",
        f"{file}{WEBM_EXT}",
        f"{file}{WAV_EXT}",
        "-loglevel",
        "error",
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE)


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
    config = speech.RecognitionConfig(language_code="en-US", audio_channel_count=1)

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