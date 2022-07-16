"""
Date: 2021-12-11
Author: Gustav Collin Rasmussen
Purpose: Store and analyze weight-training data
https://tinydb.readthedocs.io/en/latest/getting-started.html
"""

import json
from tinydb import Query, TinyDB  # type: ignore


def get_dates(table) -> list[str]:
    """Get all workout dates

    :param table: _description_
    :type table: _type_
    :return: _description_
    :rtype: list[str]
    """

    return [item["date"] for item in table]


def get_dates_and_muscle_groups(table) -> dict[str, str]:
    """Returns all workout dates with their corresponding muscle groups.

    :param table: A TinyDB table
    :type table: TinyDB table
    :return: A dictionary of workout dates and corresponding splits / musclegroup
    :rtype: dict[str, str]
    """

    return {item["date"]: item["split"] for item in table}


def show_exercises(table, date: str) -> list[str]:
    """Show all exercises for given workout date

    :param table: A TinyDB table
    :type table: TinyDB table
    :param date: Date of a given workout
    :type date: str
    :return: A list of exercises performed on a given date
    :rtype: list[str]
    """

    all_exercises_during_workout = []

    for item in table:
        if item["date"] == date:
            for k, _ in item["exercises"].items():
                all_exercises_during_workout.append(k)
    return all_exercises_during_workout


def get_all(table) -> list[dict]:
    """get all documents

    :param table: _description_
    :type table: _type_
    :return: _description_
    :rtype: list[dict]
    """

    return table.all()


def describe_workout(log, date: str) -> dict:
    """Simple summary statistics for each exercise

    :param log: _description_
    :type log: _type_
    :param date: _description_
    :type date: str
    :return: _description_
    :rtype: dict
    """

    d = {}
    for item in log:
        if item["date"] == date:
            d["Date of workout"] = date

            for k, v in item["exercises"].items():
                d[k] = f"{len(v)} sets"
    return d


def show_exercise(log, exercise: str, date: str) -> list:
    """Show detailed data for selected exercise

    :param log: _description_
    :type log: _type_
    :param exercise: _description_
    :type exercise: str
    :param date: _description_
    :type date: str
    :return: _description_
    :rtype: list
    """

    for item in log:
        if item["date"] == date:
            for k, v in item["exercises"].items():
                if k == exercise:
                    return v
    return []


def analyze_workout(table, exercise: str) -> list:
    """Deeper analysis of workout

    :param table: A TinyDB table
    :type table: TinyDB table
    :param exercise: Name of exercise to analyze
    :type exercise: str
    :return: _description_
    :rtype: list
    """

    Log = Query()
    data = table.search(Log["exercises"][exercise].exists())

    return [d["exercises"][exercise] for d in data]


def main() -> None:
    """_summary_"""

    datamodels = ["real", "simulated"]
    datatype = datamodels[0]

    data = json.load(open(file="./config.json", encoding="utf-8"))
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

    # dates_and_muscle_groups = get_dates_and_muscle_groups(table)
    # print(dates_and_muscle_groups)
    # print(show_exercises(table, "2021-12-16"))
    print(get_all(table))
    # print(describe_workout(table, "2021-12-13"))
    # show_exercise(table, "squat", "2021-12-11")
    # print(analyze_workout(table, "squat"))


if __name__ == "__main__":
    main()
