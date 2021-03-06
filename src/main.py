"""
Date: 2021-12-11
Author: Gustav Collin Rasmussen
Purpose: Expose API for training data

Doc: https://fastapi.tiangolo.com/tutorial/first-steps/

To run, execute following command from CLI:
cd src && uvicorn main:app --reload

visit URL: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, Response  # type: ignore

# import uvicorn  # type: ignore
import json
from tinydb import TinyDB  # type: ignore

from CRUD.read import get_dates, get_dates_and_muscle_groups, describe_workout, show_exercise  # type: ignore

app = FastAPI()

data = json.load(open(file="./config.json", encoding="utf-8"))
db = TinyDB(data["real_workout_database"])
table = db.table(data["real_weight_table"])

"""
datatype = "real"
db = (
    TinyDB(data["real_workout_database"])
    if datatype == "real"
    else TinyDB(data["simulated_workout_database"])
)
table = (
    db.table(data["real_weight_table"])
    if datatype == "real"
    else db.table(data["simulated_weight_table"])
)
"""


@app.get("/")
async def main_page() -> Response:
    """_summary_

    :return: _description_
    :rtype: Response
    """

    return Response("hello, athlete. Welcome to your tracker!")


@app.get("/dates")
async def get_all_dates() -> list:
    """_summary_

    :return: _description_
    :rtype: list
    """

    return get_dates(table)


@app.get("/dates_and_splits")
async def get_dates_and_splits() -> dict:
    """_summary_

    :return: _description_
    :rtype: dict
    """

    return get_dates_and_muscle_groups(table)


@app.get("/dates/{date}")
async def get_workout_description(date: str) -> HTTPException | dict:
    """_summary_

    :param date: _description_
    :type date: str
    :raises HTTPException: _description_
    :return: _description_
    :rtype: HTTPException | dict
    """

    if date not in get_dates(table):
        raise HTTPException(status_code=404, detail="Workout date not found")
    return describe_workout(table, date)


@app.get("/{date}/exercises/{exercise}")
async def get_exercise_info(exercise: str, date: str) -> list:
    """_summary_

    :param exercise: _description_
    :type exercise: str
    :param date: _description_
    :type date: str
    :return: _description_
    :rtype: list
    """

    return show_exercise(table, exercise, date)


# if __name__ == "__main__":
#     uvicorn.run(app, port=8000, host="0.0.0.0")
