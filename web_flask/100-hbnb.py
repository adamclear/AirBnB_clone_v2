#!/usr/bin/python3
"""
This module starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_list():
    """
    Displays HTML page of all State objects present
    in DB storage sorted A-Z.
    """
    allstate = storage.all(State)
    amenities = storage.all(Amenity).values()
    places = storage.all(Place)
    return render_template('100-hbnb.html', allstate=allstate,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(done):
    """
    Removes the current SQLAlchemy session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
