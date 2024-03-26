#!/usr/bin/python3
"""Starts a flask web application"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def my_text(text='is cool'):
    """Return C followed by value of text"""

    if "_" in text:
        text = text.split("_")
        text = ",".join(text)
        text = text.replace(",", " ")
    return f"Python {text}"


@app.route("/number/<int:n>")
def number(n):
    """Returns a number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_a_number_template(n=None):
    """Render HTML Page"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_even_or_odd_template(n):
    """Checks whether n is odd or even"""
    mod = n % 2

    if mod == 0:
        return render_template("6-number_odd_or_even.html",
                               num=n, status='even')
    else:
        return render_template("6-number_odd_or_even.html",
                               num=n, status='odd')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
