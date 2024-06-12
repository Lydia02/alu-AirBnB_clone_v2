#!/usr/bin/python3
""" Write a script that starts a Flask web application,
Web application is listening on 0.0.0.0, port 5000 """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """Returns list of states"""
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """Closes the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.url_map.strict_slashes = False
