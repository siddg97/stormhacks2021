from flask import Flask, request
from pymongo import MongoClient
from constants import GCS_BUCKET, TMP_DIR, WEBM_EXT, WAV_EXT
from stats import upload_file, get_stats, get_transcript
from uuid import uuid1, uuid4
import subprocess
from questions import (
    gen_questions,
    tech_question_templates,
    soft_question_templates,
    process_tech_skills,
    process_soft_skill
)
from flask.json import JSONEncoder
from bson import json_util

class MEncoder(JSONEncoder):
    def default(self, obj): return json_util.default(obj)

# mongo client
client = MongoClient('mongodb://mongo:27017/')
db = client['database']

users = db.users

# flask app
app = Flask(__name__)
app.json_encoder = MEncoder

@app.route('/api/ping', methods=['GET'])
def hello_docker():
    return { 'pong': 'Flask is running'}

@app.route('/api/results/<uid>/<type>', methods=['GET'])
def get_results(uid, type):
    """
    - files dir in = <uid>
    - file names in user doc under bucket_files key
    - fetch files, analyse audio
    - aggregate stats
    - return aggd and individual stats
    """
    user = users.find_one({ 'uid': uid })
    bucket_dir = uid
    all_stats = []

    for each in user['bucket_files']:
        file_path = f"{bucket_dir}/{each}"
        transcript = get_transcript(f'gs://{GCS_BUCKET}/{file_path}')
        stats = get_stats(transcript, each, TMP_DIR)
        all_stats.append(stats)

    num_pauses = 0
    en = 72 if type == 'bad' else 80
    wpm = 0
    for each in all_stats:
        num_pauses+= int(each['number_of_pauses'])
        wpm += int(each['words_per_min'])

    return {
        'stats': {
            'wpm': {
                'total': wpm,
                'avg': wpm /len(all_stats)
            },
            'np': {
                'total': num_pauses,
                'avg': num_pauses /len(all_stats)
            },
            'en': en,
        },
    }

def convert_to_wav(file):
    command = ['ffmpeg', '-i', file + ".webm", file + ".wav"]
    subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)

@app.route('/api/submit-answer/<uid>', methods=['POST'])
def get_stats_for_audio(uid):
    """
    1. Take sample Wave file
    2. upload to a temp directory in cloud storage, with a unique name
    3. Fetch transcripts from gcloud
    4. get stats using the .praat file
    4. return stats
    """
    webm_file = request.files['audio']
    blob_name = str(uuid4())

    users.update_one({ 'uid': uid },  {'$push': {'bucket_files': f"{blob_name}{WAV_EXT}" }})

    file_path_with_name = f'{TMP_DIR}/{blob_name}'
    wav_fp = f'{file_path_with_name}{WAV_EXT}'
    webm_fp = f'{file_path_with_name}{WEBM_EXT}'

    webm_file.save(webm_fp)

    # convert to webm to wav file
    convert_to_wav(file_path_with_name)

    # upload to bucket
    upload_file(GCS_BUCKET, f'{uid}/{blob_name}{WAV_EXT}', wav_fp)
    print('[INFO]: done uploading')

    return {}, 200

@app.route('/api/gen-questions', methods=['GET'])
def get_questions_for_jd():
    body = request.get_json(force=True)
    jd = body['jobdesc']
    uid = str(uuid1())
    user_doc = {
        'job_desc': jd,
        'uid': uid,
        'bucket_files': [],
    }
    users.insert_one(user_doc)

    t_skills = process_tech_skills(jd)
    s_skills = process_soft_skill(jd)
    print(uid)
    return {
        'uid': uid,
        'soft': gen_questions(s_skills, soft_question_templates),
        'tech': gen_questions(t_skills, tech_question_templates)
    }, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


