import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session url_for
from intake.db import get_db

bp = Blueprint('form', __name__, url_prefix='/volunteer')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form["name"]
        address = request.form["address"]
        city = request.form["city"]
        state = request.form["state"]
        zip = request.form["zip"]
        home_phone = request.form["home_phone"]
        occupation = request.form["occupation"]
        employer = request.form["employer"]
        cell_phone = request.form["cell_phone"]
        email = request.form["email"]
        dob = request.form["dob"]

        # A lot of data cleaning will probably happen here.
        if not name:
            error = "Name is required."
        
        if error is None:
            # TODO: build out the full intake form to match the schema.
            pass