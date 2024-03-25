#!/usr/bin/python3
"""Starts a flask web application"""

from flask import Flask

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
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
