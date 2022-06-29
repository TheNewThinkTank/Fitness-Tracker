"""
Date: 2021-12-13
Author: Gustav Collin Rasmussen
Purpose: Store weight-training data
https://tinydb.readthedocs.io/en/latest/getting-started.html
"""

import glob
import json
import os
import pathlib

from tinydb import TinyDB  # type: ignore

from src.helpers.lookup import get_year_and_month


def insert_log(table, log_path) -> None:
    """Store training log: log_path in database table.

    :param table: A TinyDB table
    :type table: TinyDB table
    :param log_path: A path to the workout log file
        that will be inserted into the table
    :type log_path: string
    """

    with open(*log_path) as rf:
        json_content = json.load(rf)
    table.insert(json_content)


def insert_all_logs(table, folderpath) -> None:
    """Store all training logs in database.

    :param table: A TinyDB table
    :type table: TinyDB table
    :param folderpath: A path to the workout log folder,
        from where each file will be inserted into the table
    :type folderpath: string
    """

    p = pathlib.Path(folderpath)
    all_files = os.listdir(p)
    for f in all_files:
        insert_log(table, p / f)


def insert_specific_log(date, table, workout_number=1) -> None:
    """Store a specific training log in database.

    :param date: string of date in format YYYY-MM-DD
    :type date: str
    :param table: A TinyDB table
    :type table: TinyDB table
    :param workout_number: unique identifier of the workout on a given day,
        in case of multiple workouts. Defaults to 1
    :type workout_number: int, optional
    """

    YEAR, MONTH = get_year_and_month(date)

    if workout_number == 1:
        log_path = glob.glob(
            f"data/log_archive/JSON/{YEAR}/{MONTH}/*training_log_{date}.json"
        )
    else:
        log_path = glob.glob(
            f"data/log_archive/JSON/{YEAR}/{MONTH}/*training_log_{date}_{workout_number}.json"
        )
    insert_log(table, log_path)


def main() -> None:
    """Insert all simulated- or 1 or more real training logs"""

    import argparse
    import logging

    parser = argparse.ArgumentParser()
    parser.add_argument("--datatype", type=str, required=True)
    parser.add_argument("--dates", type=str)
    parser.add_argument("--workout_number", type=int)
    args = parser.parse_args()
    datatype = args.datatype  # real/simulated
    dates = args.dates  # 2022-02-03,2022-02-05
    workout_number = args.workout_number

    pathlib.Path("logs/").mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        filename="logs/insert.log",
        filemode="w",
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)
    logging.info("Running %s ...", "/".join(__file__.split("/")[-4:]))

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

    logging.info("datatype: %s", datatype)
    logging.debug("db: %s", db)
    logging.debug("table: %s", table)

    if datatype == "real":
        logging.info("workout date(s): %s", dates)
        for date in dates.split(","):
            if args.workout_number is None:
                insert_specific_log(date, table)
            else:
                insert_specific_log(date, table, workout_number)
                logging.info("workout number: %s", workout_number)

    elif datatype == "simulated":
        insert_all_logs(table, "data/simulated/")

    else:
        logging.error("Unsupported value for datatype: %s", datatype)


if __name__ == "__main__":
    main()
