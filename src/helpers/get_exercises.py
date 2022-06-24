"""_summary_
"""

import json
from typing import Dict

import yaml  # type: ignore


def get_available_exercises(training_catalogue: str, split: str) -> Dict:
    """Fetch musclegroup-exercises catalogue

    :param training_catalogue: Exercises available for each musclegroup
    :type training_catalogue: String
    :param split: Name of musclegroup
    :type split: String
    :return: A dictionary of available exercises for a given split / musclegroup
    :rtype: Dictionary
    """
    with open(training_catalogue, "r") as rf:
        available_exercises = yaml.load(rf, Loader=yaml.FullLoader)
    return available_exercises[split]


def main():
    """_summary_"""
    splits: list = ["back"]  # , "chest", "legs", "shoulders"]

    data = json.load(open(file="./config.json", encoding="utf-8"))
    training_catalogue = data["training_catalogue"]

    for split in splits:
        print(get_available_exercises(training_catalogue, split))


if __name__ == "__main__":
    main()
