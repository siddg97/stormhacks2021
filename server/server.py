from utils import delete_local_file, convert_to_wav, upload_file
from flask import Flask, request
from constants import GCS_BUCKET, TMP_DIR, WEBM_EXT, WAV_EXT
from uuid import uuid1, uuid4

# flask app
app = Flask(__name__)

@app.route('/api/ping', methods=['GET'])
def ping():
    return { 'pong': 'pong' }, 200

@app.route('/api/submit', methods=['POST'])
def submit_answer():
    """
    1. Take sample Wave file
    2. upload to a temp directory in cloud storage, with a unique name
    """
    webm_file = request.files['audio']
    blob_name = str(uuid4())
    file_path = f'{TMP_DIR}/{blob_name}'
    wav_file_path = f'{file_path}{WAV_EXT}'
    webm_file_path = f'{file_path}{WEBM_EXT}'

    print('[INFO]: Saving .webm file')
    webm_file.save(webm_file_path)

    # convert to webm to wav file
    convert_to_wav(file_path)
    print('[INFO]: Converting .webm to .wav file')

    # upload to bucket
    upload_file(GCS_BUCKET, f'{blob_name}{WAV_EXT}', wav_file_path)
    print('[INFO]: Uploaded .wav file to GCS bucket')

    # cleanup webm and wav file in temp directory
    print('[INFO]: Cleaning up local temp directory')
    delete_local_file(webm_file_path)
    delete_local_file(wav_file_path)
    print('[INFO]: Cleanup complete !!')
    return {}, 200


# @app.route('/api/results/<uid>/<type>', methods=['GET'])
# def get_results(uid, type):
#     """
#     - files dir in = <uid>
#     - file names in user doc under bucket_files key
#     - fetch files, analyse audio
#     - aggregate stats
#     - return aggd and individual stats
#     """
#     user = users.find_one({ 'uid': uid })
#     bucket_dir = uid
#     all_stats = []

#     for each in user['bucket_files']:
#         file_path = f"{bucket_dir}/{each}"
#         transcript = get_transcript(f'gs://{GCS_BUCKET}/{file_path}')
#         stats = get_stats(transcript, each, TMP_DIR)
#         all_stats.append(stats)

#     num_pauses = 0
#     en = 72 if type == 'bad' else 80
#     wpm = 0
#     for each in all_stats:
#         num_pauses+= int(each['number_of_pauses'])
#         wpm += int(each['words_per_min'])

#     return {
#         'stats': {
#             'wpm': {
#                 'total': wpm,
#                 'avg': wpm /len(all_stats)
#             },
#             'np': {
#                 'total': num_pauses,
#                 'avg': num_pauses /len(all_stats)
#             },
#             'en': en,
#         },
#     }

# @app.route('/api/submit-answer/<uid>', methods=['POST'])
# def get_stats_for_audio(uid):
#     """
#     1. Take sample Wave file
#     2. upload to a temp directory in cloud storage, with a unique name
#     3. Fetch transcripts from gcloud
#     4. get stats using the .praat file
#     4. return stats
#     """
#     webm_file = request.files['audio']
#     blob_name = str(uuid4())

#     users.update_one({ 'uid': uid },  {'$push': {'bucket_files': f"{blob_name}{WAV_EXT}" }})

#     file_path_with_name = f'{TMP_DIR}/{blob_name}'
#     wav_fp = f'{file_path_with_name}{WAV_EXT}'
#     webm_fp = f'{file_path_with_name}{WEBM_EXT}'

#     webm_file.save(webm_fp)

#     # convert to webm to wav file
#     convert_to_wav(file_path_with_name)

#     # upload to bucket
#     upload_file(GCS_BUCKET, f'{uid}/{blob_name}{WAV_EXT}', wav_fp)
#     print('[INFO]: done uploading')

#     return {}, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


