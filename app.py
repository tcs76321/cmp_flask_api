from flask import render_template
from flask_cors import CORS

from analyses import *

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route("/1metabolite/<metabolite>/<level>", methods=["GET"])
def singleMetabolite(metabolite, level):
    try:
        checked_level = int(level)
        return singleAnalysis(metabolite, checked_level)
    except ValueError:
        return "Your level value doesn't seem to be a number"


@app.route("/comprehensive/version1", methods=["POST"])
def fullCMP():
    try:
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
            return fullAnalysis(json)
        else:
            return 'Content-Type not supported!'
    except Exception:
        return "something went wrong"


if __name__ == '__main__':
    app.run()
