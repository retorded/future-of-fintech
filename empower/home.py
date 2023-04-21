from flask import Blueprint, render_template
import empower.db as db

bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    db.update_plans_table()

    return render_template('home/index.html')

