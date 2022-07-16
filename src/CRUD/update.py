"""
Date: 2022-07-01
Author: Gustav Collin Rasmussen
Purpose: Update or delete weight-training data
"""

import json
from tinydb import TinyDB  # type: ignore


def cleanup(db, table, action: str) -> None:
    """Update, remove or truncate database

    :param db: _description_
    :type db: _type_
    :param table: _description_
    :type table: _type_
    :param action: _description_
    :type action: str
    """

    # TODO: implement update and remove actions
    if action == "update":
        # table.update({"reps": 10}, Item.exercises == "squat")
        pass

    if action == "remove":
        # table.remove(exercises.squat < 5)
        pass

    if action == "truncate":
        # table.truncate()
        # assert table.all() == []
        pass


def main() -> None:
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

    cleanup(db, table, action="truncate")


if __name__ == "__main__":
    main()
