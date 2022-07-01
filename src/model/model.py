"""
    Date: 2021-12-21
    Author: Gustav Collin Rasmussen
    Purpose: Train a linear-regression model on simulated weight-training data,
             using the Scikit Learn library
"""

from datetime import datetime
import json
import pandas as pd  # type: ignore

import pathlib
from typing import Tuple, List

# from sklearn import linear_model
from tinydb import TinyDB  # type: ignore


def get_df(
    log,
    splits: list = ["chest", "push", "chest_and_back"],
    exercise: str = "barbell_bench_press",
) -> pd.DataFrame:
    """Return one consolidated Pandas dataframe containing workout date and training data
    for specified split(s) and exercise

    :param log: _description_
    :type log: _type_
    :param splits: _description_, defaults to ["chest", "push", "chest_and_back"]
    :type splits: list, optional
    :param exercise: _description_, defaults to "barbell_bench_press"
    :type exercise: str, optional
    :return: _description_
    :rtype: pd.DataFrame
    """
    frames = []
    for item in log:
        if any(x in item["split"] for x in splits):
            if exercise in item["exercises"].keys():
                df = pd.DataFrame(item["exercises"][exercise])
                df["date"] = item["date"]
                frames.append(df)
    return pd.concat(frames)


def calc_volume(df: pd.DataFrame) -> pd.DataFrame:
    """sets times reps times load

    :param df: _description_
    :type df: pd.DataFrame
    :return: _description_
    :rtype: pd.DataFrame
    """

    df_copy = df.copy()
    num_of_sets_df = df_copy.groupby("date")[["set no."]].agg("max")
    reps_df = df_copy.groupby("date")[["reps"]].agg("max")
    df_copy["weight"] = df_copy["weight"].str.strip(" kg").astype(float)
    weight_df = df_copy.groupby("date")[["weight"]].agg("max")
    df_res = pd.concat([num_of_sets_df, reps_df, weight_df], axis=1)
    df_res["volume"] = df_res["set no."] * df_res["reps"] * df_res["weight"]

    return df_res.drop(["set no.", "reps", "weight"], axis=1)


def one_rep_max_estimator(df) -> pd.DataFrame:
    """The ACSM (American College of Sports Medicine) protocol
    is used to implement the 1RM estimation

    :param df: _description_
    :type df: pd.DataFrame
    :return: _description_
    :rtype: pd.DataFrame
    """

    df_copy = df.copy()

    df_copy["1RM"] = df["weight"].str.strip(" kg").astype(float) / (
        (100 - df["reps"] * 2.5) / 100
    )
    return df_copy.groupby("date")[["1RM"]].agg("max")


def get_data(df, y_col="1RM") -> Tuple[List[float], List[float]]:
    """Get workout-timestamps and 1RM estimates

    :param df: Pandas dataframe with workout-timestamps
        and either 1RM estimates or volume
    :type df: pd.DataFrame
    :param y_col: String signifying whether to use 1RM estimates or volume
    :type y_col: str
    :return: workout-timestamps and either 1RM estimates or volume
    :rtype: Tuple[List[float], List[float]]
    """

    date_strs = df.index.tolist()  # workout-dates
    x = [datetime.fromisoformat(i).timestamp() for i in date_strs]

    match y_col:
        case "1RM":
            y = df["1RM"].tolist()  # max 1RM estimate in kg
            y = [float("{:.2f}".format(x)) for x in y]
        case "volume":
            y = df["volume"].tolist()  # volume in kg
        case _:
            raise ValueError

    return x, y


def main():
    """Prepare dfs, calc 1RM and do linear regression."""
    import logging

    pathlib.Path("logs/").mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        filename="logs/model.log",
        filemode="w",
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)
    logging.info("Running %s ...", "/".join(__file__.split("/")[-4:]))
    logger1 = logging.getLogger("model.area1")
    logger2 = logging.getLogger("model.area2")

    data_models = ["real", "simulated"]
    datatype = data_models[0]

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

    logger1.info("data_model: %s", datatype)
    logger1.debug("db: %s", db)
    logger1.debug("table: %s", table)

    df = get_df(table)
    df_volume = calc_volume(df)
    df_1rm = one_rep_max_estimator(df)
    x, y = get_data(df_1rm)
    # x, y = get_data(df_volume, y_col="volume")

    # logger2.info("df.head(): %s", df.head())
    logger2.info("df_1rm.head(): %s", df_1rm.head())
    logger2.info("df_volume: %s", df_volume)
    logger2.info("x, y: %s, %s", x, y)


if __name__ == "__main__":
    main()
