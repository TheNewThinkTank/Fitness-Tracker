"""
Date: 2021-12-11
Author: Gustav Collin Rasmussen
Purpose: Store and analyze weight-training data
https://tinydb.readthedocs.io/en/latest/getting-started.html
"""

import json
from typing import Dict, List
from tinydb import Query, TinyDB  # type: ignore


def get_dates_and_muscle_groups(table) -> Dict:
    """Returns all workout dates with their corresponding muscle groups.

    :param table: A TinyDB table
    :type table: TinyDB table
    :return: A dictionary of workout dates and corresponding splits / musclegroup
    :rtype: Dictionary
    """
    return {item["date"]: item["split"] for item in table}


def show_exercises(table, date: str) -> List:
    """Show all exercises for given workout date

    :param table: A TinyDB table
    :type table: TinyDB table
    :param date: Date of a given workout
    :type date: String
    :return: A list of exercises performed on a given date
    :rtype: List
    """

    all_exercises_during_workout = []

    for item in table:
        if item["date"] == date:
            for k, _ in item["exercises"].items():
                all_exercises_during_workout.append(k)
    return all_exercises_during_workout


def get_all(log):
    """get all documents"""
    return log.all()


def describe_workout(log, date) -> Dict:
    """Simple summary statistics for each exercise"""

    d = {}
    for item in log:
        if item["date"] == date:
            d["Date of workout"] = date

            for k, v in item["exercises"].items():
                d[k] = f"{len(v)} sets"
    return d


def show_exercise(log, exercise, date) -> List:
    """Show detailed data for selected exercise"""

    for item in log:
        if item["date"] == date:
            for k, v in item["exercises"].items():
                if k == exercise:
                    return v
    return []


def analyze_workout(table, exercise: str) -> List:
    """Deeper analysis of workout

    :param table: A TinyDB table
    :type table: TinyDB table
    :param exercise: Name of exercise to analyze
    :type exercise: string
    """
    Log = Query()
    data = table.search(Log["exercises"][exercise].exists())
    return [d["exercises"][exercise] for d in data]


def main():
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
    # print(describe_workout(table, "2021-12-13"))
    # show_exercise(table, "squat", "2021-12-11")
    print(analyze_workout(table, "squat"))


if __name__ == "__main__":
    main()