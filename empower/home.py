from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from empower.db import get_db

bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    db = get_db()

    return render_template('home/index.html')
