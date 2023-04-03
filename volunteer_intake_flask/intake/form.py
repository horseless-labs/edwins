import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session url_for
from intake.db import get_db

bp = Blueprint('form', __name__, url_prefix='/volunteer')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        pass
