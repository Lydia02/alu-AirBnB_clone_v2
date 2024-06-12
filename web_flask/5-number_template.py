#!/usr/bin/python3
""" Write a script that starts a Flask web application,
Web application is listening on 0.0.0.0, port 5000 """

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """ Displaying Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Display HBNB! """
    return "HBNB"


@app.route("/c/<text>")
def text_c(text):
    """ Display C """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/")
@app.route("/python/<text>")
def text_py(text="is cool"):
    """ Display Python """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def num_n(n):
    """Displaying the number n"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def html_n(n):
    """Rendering a template to display an HTML page"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.url_map.strict_slashes = False
