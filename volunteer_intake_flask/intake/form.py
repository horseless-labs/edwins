import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from intake.db import get_db

bp = Blueprint('form', __name__, url_prefix='/volunteer')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form["username"]
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
        active = 1

        error = None

        db = get_db()

        # A lot of data cleaning will probably happen here.
        if not name:
            error = "Name is required."

        # Unsure the extent to which these will be required by Edwins
        if not address:
            address = "NA"
        if not city:
            city = "NA"
        if state == "--select a state--":
            state = "NA"
        if not zip:
            zip = "NA"
        if not home_phone:
            home_phone = "NA"
        if not occupation:
            occupation = "NA"
        if not employer:
            employer = "NA"
        if not cell_phone:
            cell_phone = "NA"
        if not email:
            email = "NA"
        if not dob:
            dob = "NA"

        if error is None:
            # TODO: build out the full intake form to match the schema.
            print("Error is None")
            try:
                db.execute(
                    "INSERT INTO volunteer_small (active, name, address, city, state, zip, home_phone, occupation, employer, cell_phone, email, dob)" \
                    " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (active, name, address, city, state, zip, home_phone, occupation, employer, cell_phone, email, dob),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {name} is already registered"
            else:
                return redirect(url_for('hello'))

        flash(error)
    
    return render_template("volunteer/register.html")