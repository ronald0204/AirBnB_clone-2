#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """reload close files storage"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page: (inside the tag BODY)"""
    context = storage.all(State).values()
    return render_template('7-states_list.html', states=context)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
