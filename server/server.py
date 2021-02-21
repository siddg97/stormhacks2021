from flask import Flask, request
from constants import GCS_BUCKET, TMP_DIR, WEBM_EXT, WAV_EXT
from stats import upload_file, get_stats, get_transcript
from uuid import uuid4
import subprocess
from questions import (
    gen_questions,
    tech_question_templates,
    soft_question_templates,
    process_tech_skills,
    process_soft_skill
)

app = Flask(__name__)

def convert_to_wav(file):
    command = ['ffmpeg', '-i', file + ".webm", file + ".wav"]
    subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)

@app.route('/api/ping', methods=['GET'])
def hello_docker():
    return { 'pong': 'Flask is running'}

@app.route('/api/audio-stats', methods=['POST'])
def get_stats_for_audio():
    """
    1. Take sample Wave file
    2. upload to a temp directory in cloud storage, with a unique name
    3. Fetch transcripts from gcloud
    4. get stats using the .praat file
    4. return stats
    """
    webm_file = request.files['audio']
    blob_name = str(uuid4())

    file_path_with_name = f'{TMP_DIR}/{blob_name}'
    wav_fp = f'{file_path_with_name}{WAV_EXT}'
    webm_fp = f'{file_path_with_name}{WEBM_EXT}'

    webm_file.save(webm_fp)

    # convert to webm to wav file
    convert_to_wav(file_path_with_name)

    # upload to bucket
    upload_file(GCS_BUCKET, f'{blob_name}{WAV_EXT}', wav_fp)
    print('[INFO]: done uploading')

    # retrieve transcripts
    transcript = get_transcript(f'gs://{GCS_BUCKET}/{blob_name}{WAV_EXT}')
    print('[INFO]: transcript received')

    # compute stats
    stats = get_stats(transcript, f'{blob_name}{WAV_EXT}', TMP_DIR)
    print('[INFO]: stats computed')

    return {
        'stats': stats
    }, 200

@app.route('/api/gen-questions', methods=['GET'])
def get_questions_for_jd():
    body = request.get_json(force=True)
    jd = body['jobdesc']
    t_skills = process_tech_skills(jd)
    s_skills = process_soft_skill(jd)

    return {
        'soft': gen_questions(s_skills, soft_question_templates),
        'tech': gen_questions(t_skills, tech_question_templates)
    }, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# match_technical = process_tech_skills(sample)
# tq = gen_questions(match_technical, tech_question_templates)
# print(tq)

# match_soft = process_soft_skill(sample)
# sq = gen_questions(match_soft, soft_question_templates)
# print(sq)