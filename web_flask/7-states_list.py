#!/usr/bin/python3
""" starts a flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception):
    """closes connection"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """renders an html odd or even template"""
    list_states = storage.all(State).values()
    return render_template('7-states_list.html', states=list_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
