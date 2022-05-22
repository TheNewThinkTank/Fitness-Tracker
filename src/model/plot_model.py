"""
Date: 2021-12-27
Author: Gustav Collin Rasmussen
Purpose: Plot weight-training data with fit
"""

import json
import os
import sys
from datetime import datetime

# from pprint import pprint as pp
import matplotlib.pyplot as plt  # type: ignore

# import matplotlib.ticker as mticker  # type: ignore
import seaborn as sns  # type: ignore
from tinydb import TinyDB  # type: ignore

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from model import get_data, get_df, one_rep_max_estimator


def create_plots(datatype: str, x: list, y: list, exercise: str) -> None:
    """Plot training data with fit"""

    plt.figure(figsize=(8, 8))

    x_prg1, x_prg2 = x[:10], x[10:]
    y_prg1, y_prg2 = y[:10], y[10:]

    # Only add confidence intervals if there are sufficient data points
    if len(x) < 5:
        sns.set_theme()
        ax = sns.scatterplot(x=x, y=y)
        ax.set_title(f"{exercise}")
    else:
        # ax = sns.regplot(x=x, y=y, ci=68, truncate=False)
        ax = sns.regplot(x=x_prg1, y=y_prg1, ci=68, truncate=False, label="Program_1")
        sns.regplot(x=x_prg2, y=y_prg2, ci=68, truncate=True, label="Program_2")
        ax.set_title(f"{exercise}")

    xticks = ax.get_xticks()
    xticks_dates = [datetime.fromtimestamp(x).strftime("%Y-%m-%d") for x in xticks]

    ax.set_xticklabels(xticks_dates)
    plt.ylim(0, max(y) + 5)
    plt.xticks(rotation=45)
    ax.set_ylabel("1 RM estimates [kg]")
    ax.legend(loc="lower right")
    # plt.savefig(f"img/{datatype}_fitted_data_{exercise}.png")
    plt.savefig(f"img/{datatype}_fitted_data_{exercise}_splines.png")
    plt.clf()  # clear figure before next plot


def main() -> None:
    """Get data and create figure."""

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--datatype", type=str, required=True)  # real/simulated
    args = parser.parse_args()
    datatype = args.datatype

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

    splits_and_key_exercises = [
        (["chest", "push"], "barbell_bench_press"),
        (["back", "pull"], "seated_row"),
        (["legs"], "squat"),
        (["legs"], "deadlift"),
        # (["legs"], "legpress"),
    ]

    for splits, exercise in splits_and_key_exercises:

        df = get_df(table, splits, exercise)
        df_1rm = one_rep_max_estimator(df)
        x, y = get_data(df_1rm)
        # print(x, y)
        create_plots(datatype, x, y, exercise)


if __name__ == "__main__":
    main()
