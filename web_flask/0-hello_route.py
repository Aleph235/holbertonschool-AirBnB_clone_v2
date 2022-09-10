#!/usr/bin env/python3
"""flask simple application"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_HBNB():
    """hello hbnb return string"""
    return "Hello HBNB!"

if __name__=='__main__':
    app.run(host="0.0.0.0")
    