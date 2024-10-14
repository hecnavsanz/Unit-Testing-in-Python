from flask import Flask

app = Flask(__name__)


@app.route("/")
def say_hi():
    pass
