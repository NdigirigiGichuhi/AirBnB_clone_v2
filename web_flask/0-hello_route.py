#!/usr/bin/python3
"""The Flask Framework"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """
    Routing to root, strict_slashes means the
    URL works when it ends with or without the slash (/)
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
