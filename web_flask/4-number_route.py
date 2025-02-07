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


@app.route("/c/<text>", strict_slashes=False)
def Display_C(text):
    """C return string"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def Display_Python(text="is cool"):
    """Python return string"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def Display_Int(n):
    """If not int don't distplay"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
