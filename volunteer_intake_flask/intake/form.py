import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from intake.db import get_db

bp = Blueprint('form', __name__, url_prefix='/volunteer')

def stringify_checkbox(checkbox):
    str_checkbox = ', '.join(checkbox)
    return str_checkbox

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        active = 1
        name = request.form["username"]
        address = request.form["address"] or "NA"
        city = request.form["city"] or "NA"
        state = request.form["state"] or "--select a state--"
        zip = request.form["zip"] or "NA"
        home_phone = request.form["home_phone"] or "NA"
        occupation = request.form["occupation"] or "NA"
        employer = request.form["employer"] or "NA"
        cell_phone = request.form["cell_phone"] or "NA"
        email = request.form["email"] or "na@na.com"
        dob = request.form["dob"] or "NA"

        times = request.form.getlist("times[]") or ["NA"]
        times = stringify_checkbox(times)

        selected_interests = request.form.getlist("interests[]") or ["NA"]
        other_interests = request.form.get("other_interests") or "NA"
        selected_interests = stringify_checkbox(selected_interests)

        skills = request.form.get("skills") or "NA"
        experience = request.form.get("experinece") or "NA"

        oef = request.form.getlist("oef[]") or ["NA"]
        oef = stringify_checkbox(oef)

        students_lives = request.form.getlist("students_lives[]") or ["NA"]
        other_students_lives = request.form.get("other_students_lives") or "NA"
        students_lives = stringify_checkbox(students_lives)

        class_education = request.form.getlist("class_education[]") or ["NA"]
        guest_speaker = request.form.get("guest_speaker") or "NA"
        class_education = stringify_checkbox(class_education)

        facilities = request.form.getlist("facilities[]") or ["NA"]
        clerical_advo = request.form.getlist("clerical_advo[]") or ["NA"]
        facilities = stringify_checkbox(facilities)
        clerical_advo = stringify_checkbox(clerical_advo)

        error = None

        db = get_db()

        # A lot of data cleaning will probably happen here.
        if not name:
            error = "Name is required."

        if error is None:
            # TODO: build out the full intake form to match the schema.
            print("Error is None")
            try:
                db.execute(
                    "INSERT INTO volunteer (active, name, address, city, state, zip, home_phone, occupation, employer, cell_phone, email, dob, \
                    times, selected_interests, other_interests, skills, experience, oef, students_lives, other_students_lives, class_education, \
                    guest_speaker, facilities, clerical_advo) \
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (active, name, address, city, state, zip, home_phone, occupation, employer, cell_phone, email, dob, times, selected_interests,
                     other_interests, skills, experience, oef, students_lives, other_students_lives, class_education, guest_speaker, facilities, clerical_advo),
                )
                #db.commit()
            except db.IntegrityError:
                error = f"User {name} is already registered"
            else:
                return redirect(url_for('hello'))

        flash(error)
    
    return render_template("volunteer/register.html")