"""
Date: 2021-12-19
Author: Gustav Collin Rasmussen
Purpose: Plot weight-training data
"""

import json

import matplotlib.pyplot as plt  # type: ignore
import pandas as pd  # type: ignore
import seaborn as sns  # type: ignore
from tinydb import TinyDB  # type: ignore

from CRUD.training import show_exercise  # type: ignore
from helpers.get_exercises import get_available_exercises  # type: ignore


def get_data(date, split) -> dict:
    """Prepare pandas dataframes with training data for plotting"""

    datatype = "real"
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
    training_catalogue = data["training_catalogue"]
    exercises = get_available_exercises(training_catalogue, split)

    return {
        ex: df
        for ex in exercises
        if not (df := pd.DataFrame(data=show_exercise(table, ex, date))).empty
    }


def create_barplots(dfs, date):
    """Plot training data for specific date"""

    # TODO: highten legend transparency
    # TODO: set figure-level x- and y labels ("Set No." and "Repetitions")

    sns.set_theme(style="white", context="talk")
    f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(9, 7), sharex=True)

    # debugging
    # keys = list(dfs.keys())
    # values = list(dfs.values())
    # for k, v in zip(keys, values):
    #     print(k)
    #     print(v)

    sns.barplot(
        x=dfs["squat"]["set no."],
        y=dfs["squat"]["reps"],
        hue=dfs["squat"]["weight"],
        palette="rocket",
        ax=ax1,
    )
    ax1.axhline(0, color="k", clip_on=False)
    ax1.set_ylabel("squat")
    ax1.bar_label(ax1.containers[0])

    sns.barplot(
        x=dfs["deadlift"]["set no."],
        y=dfs["deadlift"]["reps"],
        hue=dfs["deadlift"]["weight"],
        palette="vlag",
        ax=ax2,
    )
    ax2.axhline(0, color="k", clip_on=False)
    ax2.set_ylabel("deadlift")
    ax2.bar_label(ax2.containers[0])

    sns.barplot(
        x=dfs["leg_extention"]["set no."],
        y=dfs["leg_extention"]["reps"],
        hue=dfs["leg_extention"]["weight"],
        palette="deep",
        ax=ax3,
    )
    ax3.axhline(0, color="k", clip_on=False)
    ax3.set_ylabel("leg_extention")
    ax3.bar_label(ax3.containers[0])

    sns.despine(bottom=True)
    plt.setp(f.axes, yticks=[])
    plt.tight_layout(h_pad=2)
    plt.title(f"Workout date: {date}")

    # plt.ylabel("Repetitions")
    # plt.xlabel("Set No.")

    sns.move_legend(ax1, "upper right", bbox_to_anchor=(1, 1))
    # sns.move_legend(ax2, "center right", bbox_to_anchor=(1, 1))
    sns.move_legend(ax3, "center right", bbox_to_anchor=(1, 1))

    # ax3.legend(fancybox=True, framealpha=0.5)
    plt.savefig(f"img/workout_{date}.png")


def main():
    """Get data and create figure."""
    dates = [
        "2021-12-11",
        # "2022-03-14",
        "2022-05-28",
    ]
    for date in dates:
        create_barplots(get_data(date, "legs"), date)
    # plt.show()


if __name__ == "__main__":
    main()
