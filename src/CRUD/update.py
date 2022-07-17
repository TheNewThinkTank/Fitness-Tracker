"""
Date: 2022-07-01
Author: Gustav Collin Rasmussen
Purpose: Update or delete weight-training data
"""

import json
from tinydb import TinyDB, Query  # type: ignore


def update_table(table) -> None:
    """_summary_"""

    Workout = Query()
    # Exercise = Query()
    # table.search(
    #     Workout.exercises.any(
    #         Exercise.chinup == [{"reps": 6, "set no.": 1, "weight": "13.43 kg"}]
    #     )
    # )

    table.search(Workout.exercises.Exercise.fragment({"foo": True, "bar": False}))

    # table.search(Check["json-object"]["test"].exists())
    # table.update({"reps": 10}, Item.exercises.chinup.reps == 6)


def remove_from_table(table) -> None:
    """_summary_

    :param table: _description_
    :type table: _type_
    """
    # table.remove(exercises.squat < 5)
    pass


def truncate_table(table) -> None:
    """truncate table

    :param table: _description_
    :type table: _type_
    """

    table.truncate()
    assert table.all() == []


def main() -> None:
    """_summary_"""

    datamodels = ["real", "simulated"]
    datatype = datamodels[1]

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

    # print(db, table)
    update_table(table)
    # remove_from_table(table)
    # truncate_table(table)


if __name__ == "__main__":
    main()
