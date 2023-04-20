from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from empower.db import get_db


bp = Blueprint('transformer', __name__, url_prefix='/transformer')


# TODO Creating the view for the user to select/upload/access consumption data EITHER via API or stored locally
@bp.route('/consumption', methods=('GET', 'POST'))
def consumption():
    if request.method == 'POST':
        consumer = request.form['consumer']

        # TODO fetch consumer data from db / API
        error = None

        if consumer is None:
            error = 'Oops! We need your personal power consumption to give you the best deal for you!'

        if error is None:
            return redirect(url_for('providers'))

        flash(error)

    return render_template('transformer/consumption.html')


# TODO Creating the view for showing the user what the cost of each provided is
@bp.route('/providers', methods=('GET', 'POST'))
def providers():
    return None
