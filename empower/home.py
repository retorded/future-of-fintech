from flask import Blueprint, flash, g, redirect, render_template, request, url_for
import empower.db as db

bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    db.update_plans_table()

    return render_template('home/index.html')

