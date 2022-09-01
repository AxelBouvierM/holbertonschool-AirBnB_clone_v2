#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """
    List states and storage
    """
    flag = 0
    states_l = storage.all("State").values()
    return render_template("9-states.html", states_l=states_l, flag=flag)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    List states and storage
    """
    flag = 1
    states_l = storage.all("State").values()
    for state in states_l:
        if state.id == id:
            return render_template("9-states.html", state=state, flag=flag)
    return render_template("9-states.html", state=None, flag=flag)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)