#!/usr/bin/python3
"""Importing Flask to run the web app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask("__name__")


@app.route('/states_list', strict_slashes=False)
def display_state():
    """Render state_list html page to display State created"""
    state = stirage.all()
    return render_template('7-state_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Methodto remove current SQLalchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

