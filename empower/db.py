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
        g.db = sqlite3.connect(

            # current_app points to Flask app handling request (get_db is called when app has been created, therefore we can use it)
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


def populate_db():
    db = get_db()

    # here we populate the "plans" table with data from an API
    response_api = requests.get('https://future-of-fintech-v2023.vercel.app/api/providers')

    if response_api.status_code == 200:
        plans = json.loads(response_api.text)

        priceKeys = ["spotPrice", "variablePrice", "fixedPrice"]
        periodKeys = ["fixedPricePeriod", "variablePricePeriod"]

        # Looping through all the plans
        for i in range(0, len(plans)):
            planId = i,
            provider = plans[i]['name']
            pricingModel = plans[i]['pricingModel']
            monthlyFee = plans[i]['monthlyFee']
            for k in priceKeys:
                if k in plans[i]:
                    price = plans[i][k]
                else:
                    # NULL is not an allowed datatype as per the schema.sql for price col
                    price = "NULL"
            for p in periodKeys:
                if p in plans[i]:
                    period = plans[i][p]
                else:
                    price = "NULL"

            db.execute(
                "INSERT INTO plans (id, provider, pricingModel, monthlyFee, price, period) VALUES (?, ?, ?, ?, ?)",
                (planId, provider, pricingModel, monthlyFee, price, period),
            )
            db.commit()
    else:
        click.echo('Could not fetch provider data from API')


def init_db():
    db = get_db()

    # opens the file (with SQL) that is relative to the empower package
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    # here we call the help function populate_db that will populate the database
    populate_db()




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
