import sqlite3
import requests
import json

import click
from flask import current_app, g


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


def get_row_tuple_from_json(plan):
    priceKeys = ["spotPrice", "variablePrice", "fixedPrice"]
    periodKeys = ["fixedPricePeriod", "variablePricePeriod"]

    if plan:
        provider = plan['name']
        pricingModel = plan['pricingModel']
        monthlyFee = plan['monthlyFee']
        for k in priceKeys:
            if k in plan:
                price = plan[k]
        for p in periodKeys:
            if p in plan:
                period = plan[p]
            else:
                period = "NULL"
    else:
        return "NULL", "NULL", "NULL", "NULL", "NULL"

    return (provider, pricingModel, monthlyFee, price, period)


def update_plans_table():
    # This function should check if the data in the table "plans" is updated to the API for providers
    # if not, populate and/or make changes
    db = get_db()

    response_api = requests.get('https://future-of-fintech-v2023.vercel.app/api/providers')

    if response_api.status_code == 200:
        plans = json.loads(response_api.text)

        for plan in plans:
            # a tuple containing record values to input into the database
            rowTuple = get_row_tuple_from_json(plan)

            # we now perform an insert in such a way that it ignores provider plans already in the database
            db.execute(
                "INSERT OR IGNORE INTO plans (provider, pricingModel, monthlyFee, price, period) VALUES (?, ?, ?, ?, ?)",
                rowTuple
            )
            db.commit()

    else:
        click.echo('Could not fetch provider data from API')


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
