#!/usr/bin env/python3
"""flask simple application"""
from flask import Flask, render_template

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

@app.route("/number/<int:n>", strict_slashes=False)
def Display_Int(n):
    """If not int don't distplay"""
    return f"{n} in a number"

@app.route("/number_template/<int:n>", strict_slashes=False)
def Display_html_Int(n):
    """If not int don't distplay"""
    return render_template('5-number.html', n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def Display_html_Int_is_even_or_odd(n):
    """If not int don't distplay"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__=='__main__':
    app.run(host="0.0.0.0")
