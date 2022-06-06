"""_summary_
"""

import json

import yaml


def get_available_exercises(training_catalogue, split):
    """Fetch musclegroup-exercises catalogue"""
    with open(training_catalogue, "r") as rf:
        available_exercises = yaml.load(rf, Loader=yaml.FullLoader)
    return available_exercises[split]


def main():
    splits: list = ["back"]  # , "chest", "legs", "shoulders"]

    data = json.load(open(file="./config.json", encoding="utf-8"))
    training_catalogue = data["training_catalogue"]

    for split in splits:
        print(get_available_exercises(training_catalogue, split))


if __name__ == "__main__":
    main()
