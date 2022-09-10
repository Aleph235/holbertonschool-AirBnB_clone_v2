#!/usr/bin/python3
"""flask simple application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """hello hbnb return string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """hbnb return string"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
