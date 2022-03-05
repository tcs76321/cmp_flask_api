from flask import Flask, request, jsonify
from markupsafe import escape

from analyses import *

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Welcome to The Comprehensive Metabolic Panel API'


@app.route("/comp")
def comprehensive():
    return runComp(request.data)


if __name__ == '__main__':
    app.run()
