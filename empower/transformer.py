from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from empower.db import get_db, update_consumption_table

bp = Blueprint('transformer', __name__, url_prefix='/transformer')


@bp.route('/consumption', methods=('GET', 'POST'))
def consumption():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        db = get_db()
        error = None

        if not name:
            error = 'Name is required.'
        elif not address:
            error = 'Address is required.'

        if error is None:
            consumer = {'name': name, 'address': address}

            update_consumption_table(consumer)
            return redirect(url_for('transformer.providers'))

        flash(error)

    return render_template('transformer/consumption.html')


# TODO Creating the view for showing the user what the cost of each provided is
def get_all_plans():
    db = get_db()
    all_plans = db.execute(
        'SELECT * FROM plans'
    ).fetchall()

    return all_plans


@bp.route('/providers', methods=('GET', 'POST'))
def providers():
    return render_template('transformer/providers.html')
