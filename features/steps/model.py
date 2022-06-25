import json

from behave import Given, When, Then

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.model.model import get_df  # get_data, one_rep_max_estimator

from tinydb import TinyDB

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


@Given("A valid combination of musclegroup and exercise")
def given_combo(context):
    context.combo = ("legs", "squat")
    # TODO: check combo exists in catalog


@When("Looking up in the db")
def when_lookup(context):
    split, ex = context.combo
    context.get_df = get_df(table, split, ex)


@Then("The resulting dataframe has more than 2 entries")
def then_results(context):
    assert len(context.get_df) > 2
