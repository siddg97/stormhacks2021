from flask import Flask

app = Flask(__name__)

@app.route('/send')

@app.route('/test')
def get_current_time():
    return "this was an endpoint test"