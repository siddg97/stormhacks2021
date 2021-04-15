from app.utils.constants import GCS_BUCKET, WAV_EXT, WEBM_EXT, TMP_DIR
import subprocess
from google.cloud import speech
from app.utils.gcs import decompose_gcs_uri, read_file, upload_file
from parselmouth.praat import run_file
import pandas as pd
import numpy as np


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
    config = speech.RecognitionConfig(language_code="en-US")

    # execute the recognition API
    operation = client.long_running_recognize(config=config, audio=audio)
    print("Waiting for operation to complete...")
    # wait for 90 seconds max
    response = operation.result(timeout=90)

    confidence = []
    transcript = ""
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        confidence.append(result.alternatives[0].confidence)
        transcript = transcript + result.alternatives[0].transcript
    confidence = sum(confidence) / len(confidence)

    return transcript, confidence


def compute_stats(uri):
    if not uri:
        return None

    # download answer file
    bucket, path, name = decompose_gcs_uri(uri)
    local_path = f"{TMP_DIR}/{name}"
    read_file(bucket, path, local_path)

    # convert webm to wav file
    convert_to_wav(local_path.replace(WEBM_EXT, ""))

    # Upload wav file to gcs
    upload_file(
        bucket,
        f"{path.replace(WEBM_EXT, WAV_EXT)}",
        f"{local_path}",
    )

    # get transcript
    transcript, accuracy = get_transcript(uri)

    # compute stats
    stats = get_stats(transcript, name.replace(WEBM_EXT, WAV_EXT), TMP_DIR)
    stats = dict(**stats, accuracy=accuracy)
    return stats


def sentiment_analysis(z1):
    result = {
        "gender": "unknown",
        "mood": "unknown",
    }
    z2 = z1.strip().split()
    z3 = float(z2[7])
    if z3 > 97 and z3 <= 114:
        result["gender"] = "male"
        result["mood"] = "normal"
    elif z3 > 114 and z3 <= 135:
        result["gender"] = "male"
        result["mood"] = "reading"
    elif z3 > 135 and z3 <= 163:
        result["gender"] = "male"
        result["mood"] = "passionate"
    elif z3 > 163 and z3 <= 197:
        result["gender"] = "female"
        result["mood"] = "normal"
    elif z3 > 197 and z3 <= 226:
        result["gender"] = "female"
        result["mood"] = "reading"
    elif z3 > 226 and z3 <= 245:
        result["gender"] = "female"
        result["mood"] = "passionate"
    return result


def get_stats(text, m, p):
    sound = f"{TMP_DIR}/{m}"
    sourcerun = "app/utils/myspsolution.praat"
    path = p
    objects = run_file(
        sourcerun, -20, 2, 0.3, "yes", sound, path, 80, 400, 0.01, capture_output=True
    )
    # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
    z1 = str(objects[1])
    z2 = z1.strip().split()
    z3 = np.array(z2)
    z4 = np.array(z3)[np.newaxis]
    z5 = z4.T
    words = len(text.split())
    duration = z5[5, :]
    words_per_min = int(words / float(float(duration) / 60))

    result = sentiment_analysis(z1)

    dataset = pd.DataFrame(
        {
            # total number of syllables
            "number_of_syllables": z5[0, :],
            # pauses throughout audio file
            "number_of_pauses": z5[1, :],
            # syllables/sec (original duration of audio file)
            "rate_of_speech": z5[2, :],
            # syllables/sec (speaking duration of audio file)
            "articulation_rate": z5[3, :],
            # seconds of audio with speech
            "speaking_duration": z5[4, :],
            # Total duration of audio file
            "original_duration": z5[5, :],
            # (speaking duration)/(original duration)
            "balance": z5[6, :],
            # words/min
            "words_per_min": words_per_min,
            # mood
            "mood": result["mood"],
            # gender
            "gender": result["gender"],
        }
    )
    dataset["number_of_syllables"] = dataset["number_of_syllables"].astype(float)
    dataset["number_of_pauses"] = dataset["number_of_pauses"].astype(float)
    dataset["rate_of_speech"] = dataset["rate_of_speech"].astype(float)
    dataset["articulation_rate"] = dataset["articulation_rate"].astype(float)
    dataset["speaking_duration"] = dataset["speaking_duration"].astype(float)
    dataset["original_duration"] = dataset["original_duration"].astype(float)
    dataset["balance"] = dataset["balance"].astype(float)
    dataset["mood"] = dataset["mood"].astype(str)
    dataset["gender"] = dataset["gender"].astype(str)

    return dataset.to_dict(orient="index")[0]
