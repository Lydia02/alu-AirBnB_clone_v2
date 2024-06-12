#!/usr/bin/python3
""" Write a script that starts a Flask web application,
Web application is listening on 0.0.0.0, port 5000 """

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """ Displaying Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Display HBNB! """
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.url_map.strict_slashes = False
