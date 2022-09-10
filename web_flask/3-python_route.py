#!/usr/bin env/python3
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
    text.replace('_',' ')
    return f"C {text}"

@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def Display_Python(text = "is cool"):
    """Python return string"""
    text.replace('_',' ')
    return f"Python {text}"

if __name__=='__main__':
    app.run(host="0.0.0.0")
