'''
Helper functions for api data gets and transformation to keep other scripts clean
'''

import json
import requests


def get_plans_from_api(url) -> list[tuple]:
    response_api = requests.get(url)

    if response_api.status_code == 200:
        plans = json.loads(response_api.text)

        # a tuple containing record values to input into the database
        rowTuples = []

        for plan in plans:

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

                rowTuple = provider, pricingModel, monthlyFee, price, period
                rowTuples.append(rowTuple)
            else:
                rowTuples.append("NULL", "NULL", "NULL", "NULL", "NULL")

        return rowTuples

    return [("NULL", "NULL", "NULL", "NULL", "NULL")]


def get_consumption_from_api(url) -> list[tuple]:
    response_api = requests.get(url)

    if response_api.status_code == 200:
        cons = json.loads(response_api.text)

        rowTuples = []

        for entry in cons:

            from_dt = entry['from']
            to_dt = entry['to']
            consumption = entry['consumption']
            unit = entry['consumptionUnit']

            rowTuple = from_dt, to_dt, consumption, unit
            rowTuples.append(rowTuple)

        return rowTuples
    else:
        return [("NULL", "NULL", "NULL", "NULL", "NULL")]
