#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Routing to root, the strict_slashes ensures that
    the URL works both with or without the slash (/)
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Routing to root, the strict_slashes means the URL
    can work with or without the /
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    """Routing to C using variables"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/pthon/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display(text):
    """display "Python ", followed by the valie of the text """
    text = text.replace("-", "")
    return "Python {}".format(text.replace("-", ""))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
