from flask import Flask

app = Flask(__name__)

@app.route('/api')
def hello_docker():
    return 'Flask app is running'

@app.route('/api/test')
def get_current_time():
    return "this was an endpoint test"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')