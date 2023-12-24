#!/usr/bin/python3
""" starts a flask application"""
from flask import Flask, render_template


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
def display_c(text):
    """"
    display “C ” followed by
    the value of the text variable
    """
    return "C {}".format(text.replace("_", " ") if "_" in text else text)


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is cool"):
    """
    display “Python ” followed by
    the value of the text variable
    """
    return "Python {}".format(text.replace("_", " ") if "_" in text else text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    display arg if its a number
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """renders an html number template"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
