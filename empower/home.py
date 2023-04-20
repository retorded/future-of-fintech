from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from empower.db import update_plans_table

bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    update_plans_table()
    return render_template('home/index.html')

