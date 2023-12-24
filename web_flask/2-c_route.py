#!/usr/bin/python3
""" starts a flask application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """hello function"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def holberton():
    """displays hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display(text):
    """"
    display “C ” followed by
    the value of the text variable
    """
    return "C {}".format(text.replace("_", " ") if "_" in text else text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
