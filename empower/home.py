from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from empower.db import get_db

bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    return render_template('home/index.html')


@bp.before_app_request
def db_populated():
    db = get_db()
    provider = "Nord Energi"
    test_db_query = db.execute(
        'SELECT * FROM plans WHERE provider = ?', (provider,)
    ).fetchall()

    # if the fetchall is an empty list, the table "plans" has no rows with Nord Energi
    if len(test_db_query) == 0:
        return False
    else:
        return True
