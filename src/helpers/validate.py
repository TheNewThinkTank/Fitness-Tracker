"""_summary_
"""

import json
from pprint import pprint as pp
from typing import Optional

import pydantic


class ExercisesFormatError(Exception):
    """Custom error that is raised when Exercises doesn't have the right format."""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Workout(pydantic.BaseModel):
    """Represents a Workout from a JSON file."""

    date: str
    split: str
    exercises: dict
    gym: Optional[str]
    note: Optional[str]  # example in workout 25

    @pydantic.validator("exercises")
    @classmethod
    def exercise_valid(cls, value) -> None:
        """Validator to check whether exercises are valid"""

        if not value:
            raise ExercisesFormatError(
                value=value, message="There must be at least 1 exercises."
            )

        for exercise in value.values():
            if not exercise:
                raise ExercisesFormatError(
                    value=value, message="There must be at least 1 set."
                )

            for training_set in exercise:
                # print(training_set.keys())
                if not set(training_set.keys()) == {"set no.", "reps", "weight"}:
                    raise ExercisesFormatError(
                        value=value,
                        message=f"Each set should have: 'set no.', 'reps' and 'weight'. Got: {set(training_set.keys())}",
                    )

            # TODO: sets and reps should be integers
            # TODO: sets should start from 1, and monotonically increase to number of sets

        return value


def main() -> None:
    """Main function."""

    # Read data from a JSON file
    file = json.load(open(file="./config.json", encoding="utf-8"))
    file = file["real_workout_database"]
    # file = "src/helpers/validate.json"
    with open(file) as rf:
        data = json.load(rf)["weight_training_log"]
        # print(data["1"]["date"])
        # print(data.keys())
        workouts: list[Workout] = [Workout(**item) for item in data.values()]
        # print(workouts)
        # print(workouts[0])
        pp(workouts[0].exercises)
        # print(workouts[0].dict(exclude={"squat"}))
        # print(workouts[1].copy())


if __name__ == "__main__":
    main()
