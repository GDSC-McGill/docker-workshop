from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/data")
def data():
    return "some data"


if __name__ == "__main__":
    port = 9999
    app.run(host="0.0.0.0", port=port)
