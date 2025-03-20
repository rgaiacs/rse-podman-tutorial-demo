from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    response = jsonify({
        "msg": "Hello world!"
    })
    # This is unsafe. Do NOT use it!
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response