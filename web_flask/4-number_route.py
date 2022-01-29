#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """return Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """display C"""
    return "C %s" % escape(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_python(text):
    """display Python is cool"""

    return "Python %s" % escape(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display number"""
    return "%s is a number" % escape(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
