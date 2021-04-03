from mongo import init_mongo
from mongo.queries import create_new_user, get_user_by_id

from utils.misc import delete_local_file
from utils.gcs import upload_file
from utils.audio import convert_to_wav
from utils.constants import GCS_BUCKET, TMP_DIR, WEBM_EXT, WAV_EXT

from flask import Flask, request
from uuid import uuid4

# flask app init and mongo configuration
app = Flask(__name__)
init_mongo(app)

@app.route('/api/ping', methods=['GET'])
def ping():
    return { 'pong': 'pong' }, 200

@app.route('/api/test', methods=['GET'])
def test():
    user = create_new_user()
    user = get_user_by_id(user)
    return { 'user': user }

@app.route('/api/submit', methods=['POST'])
def submit_answer():
    """
    1. Take sample Wave file
    2. upload to a temp directory in cloud storage, with a unique name
    """
    user_id = request.cookies.get('IB-USER-ID')
    print(f'user_id: {user_id}')

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


