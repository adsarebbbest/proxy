import flask
import requests

app = flask.Flask(__name__)
target = "https://github.com/"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=["GET", "POST"])
def proxy(path: str):
    if flask.request.method == "GET":
        r = requests.get(f"{target}{path}")
        return r.content
    elif flask.request.method == "POST":
        r = requests.post(f"{target}{path}", json=flask.request.get_json())
        return r.content

app.run(host="0.0.0.0", port=8080)
