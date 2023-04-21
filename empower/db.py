import sqlite3
import requests
import json

import click
from flask import current_app, g
import empower.api_helper as api_helper


def get_db():
    # g is special object unique for each request, it might be accessed by multiple functions during request
    # connection is stored and reused
    if 'db' not in g:
        # establishes a connection to the file pointed at by DATABASE config key. File doesnt exist until db has been initalized
        # current_app points to Flask app handling request (get_db is called when app has been created, therefore we can use it)
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        # return rows that acts like dicts
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def update_plans_table():
    db = get_db()

    plans = api_helper.get_plans_from_api('https://future-of-fintech-v2023.vercel.app/api/providers')

    for plan in plans:
        db.execute(
            "INSERT OR IGNORE INTO plans (provider, pricingModel, monthlyFee, price, period) VALUES (?, ?, ?, ?, ?)",
            plan
        )
        db.commit()


def update_consumption_table():
    db = get_db()

    consumption = api_helper.get_consumption_from_api("https://future-of-fintech-v2023.vercel.app/api/consumption")

    for cons in consumption:
        db.execute(
            "INSERT OR IGNORE INTO consumption (from_dt, to_dt, consumption, unit) VALUES (?, ?, ?, ?)",
            cons
        )
        db.commit()


def init_db():
    db = get_db()

    # opens the file (with SQL) that is relative to the empower package
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


# init-db command that calls init-db
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()

    # Show a success message to user
    click.echo('Initialized the database.')


# for registering the functions with the application
def init_app(app):
    #  cleans up after returning response
    app.teardown_appcontext(close_db)

    app.cli.add_command(init_db_command)
