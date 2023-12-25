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


@app.route('/states', strict_slashes=False)
def states():
    """renders an html odd or even template"""
    list_states = storage.all(State).values()
    return render_template('7-states_list.html', states=list_states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """renders an html odd or even template"""
    try:
        list_states = storage.all(State).values()
        state = list(filter(lambda i: id == i.id, list_states))[0]
        cities = state.cities
        state_name = "State:" + state.name
        return render_template('9-states.html', states=list_states, cities=cities, state_name=state_name)
    except IndexError:
        return render_template('9-states.html', states=None, cities=None, state_name=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
