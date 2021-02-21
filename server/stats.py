from google.cloud import speech, storage
from parselmouth.praat import run_file
import pandas as pd
import numpy as np
from constants import TMP_DIR


def read_file(bucket_name, blob, destination):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob)
    blob.download_to_filename(destination)

def upload_file(bucket_name, blob, destination):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob)
    blob.upload_from_filename(destination)

def get_transcript(uri):
    """
    uri: file location in the bucket
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

    words = ""
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        words = words + result.alternatives[0].transcript
    return words


def get_stats(text, m, p):
    sound = f"{TMP_DIR}/{m}"
    sourcerun="./myspsolution.praat"
    path=p
    objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
    z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
    z2=z1.strip().split()
    z3=np.array(z2)
    z4=np.array(z3)[np.newaxis]
    z5=z4.T
    words = len(text.split())
    duration = z5[5,:]
    words_per_min = int(words/float(float(z5[5,:])/60))

    dataset=pd.DataFrame({"number_of_syllables":z5[0,:],"number_of_pauses":z5[1,:],"rate_of_speech":z5[2,:],"articulation_rate":z5[3,:],"speaking_duration":z5[4,:],
                        "original_duration":z5[5,:],"balance":z5[6,:],"words_per_min":words_per_min})
    dataset["number_of_syllables"] = dataset["number_of_syllables"].astype(float)
    dataset["number_of_pauses"] = dataset["number_of_pauses"].astype(float)
    dataset["rate_of_speech"] = dataset["rate_of_speech"].astype(float)
    dataset["articulation_rate"] = dataset["articulation_rate"].astype(float)
    dataset["speaking_duration"] = dataset["speaking_duration"].astype(float)
    dataset["original_duration"] = dataset["original_duration"].astype(float)
    dataset["balance"] = dataset["balance"].astype(float)

    return dataset.to_dict(orient='index')[0]
