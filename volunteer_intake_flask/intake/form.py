import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from intake.db import get_db

bp = Blueprint('form', __name__, url_prefix='/volunteer')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        active = 1
        name = request.form["username"]
        address = request.form["address"] or "NA"
        city = request.form["city"] or "NA"
        state = request.form["state"] or "NA"
        zip = request.form["zip"] or "NA"
        home_phone = request.form["home_phone"] or "NA"
        occupation = request.form["occupation"] or "NA"
        employer = request.form["employer"] or "NA"
        cell_phone = request.form["cell_phone"] or "NA"
        email = request.form["email"] or "NA"
        dob = request.form["dob"] or "NA"

        times = request.form.getlist("times[]") or "NA"

        selected_interests = request.form.getlist("interests[]") or "NA"
        other_interests = request.form.get("other_interests") or "NA"

        skills = request.form.get("skills") or "NA"
        experience = request.form.get("experinece") or "NA"

        oef = request.form.getlist("oef[]") or "NA"
        students_lives = request.form.getlist("students_lives[]") or "NA"
        other_students_lives = request.form.get("other_students_lives") or "NA"

        class_education = request.form.getlist("class_education[]") or "NA"
        guest_speaker = request.form.get("guest_speaker") or "NA"

        facilities = request.form.getlist("facilities[]") or "NA"
        clerical_advo = request.form.getlist("clerical_advo[]") or "NA"

        error = None

        db = get_db()

        # A lot of data cleaning will probably happen here.
        if not name:
            error = "Name is required."

        # Unsure the extent to which these will be required by Edwins
        """
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
        """

        if error is None:
            # TODO: build out the full intake form to match the schema.
            print("Error is None")
            try:
                db.execute(
                    "INSERT INTO volunteer (active, name, address, city, state, zip, home_phone, occupation, employer, cell_phone, email, dob," \
                    " times, selected_interests, other_interests, skills, experience, oef, students_lives, other_students_lives, class_education," \
                    " guest_speaker, facilities, clerical_advo)" \
                    " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (active, name, address, city, state, zip, home_phone, occupation, employer, cell_phone, email, dob, times, selected_interests,
                     other_interests, skills, experience, oef, students_lives, other_students_lives, class_education, guest_speaker, facilities, clerical_advo),
                )
                #print(selected_interests)
                #print(other_interests)
                #db.commit()
            except db.IntegrityError:
                error = f"User {name} is already registered"
            else:
                return redirect(url_for('hello'))

        flash(error)
    
    return render_template("volunteer/register.html")