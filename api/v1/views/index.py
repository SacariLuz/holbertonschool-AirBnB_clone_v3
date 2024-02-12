#!/usr/bin/python3
"""
first answer
"""

from flask import jsonify
from api.v1.views import app_views
from console import classes
from models import storage
from models.base_model import BaseModel


@app_views.route('/status', strict_slashes=False)
def status():
    """
    successful output with JSON
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def some_stats():
    """
    list all classes by type
    """
    tables = {"Amenity": 'amenities',
              "City": 'cities',
              "Place": 'places',
              "Review": 'reviews',
              "State": 'states',
              "User": 'users'}

    stats_class = {}

    stats_class = {f'{tables[k]}': storage.count(v)
                   for k, v in classes.items() if v != BaseModel}
    return jsonify(stats_class)
