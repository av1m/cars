# coding: utf-8
import logging

from behave import *

import foods.kebab  # type: ignore
import foods.pizza  # type: ignore
from foods.formula import Formula

logger = logging.getLogger(__name__)
use_step_matcher("parse")

foods_ = []


@given(
    "Mister Patate's favorite foods (a {food} is represented by a {sauce} and {price})"
)
def step_impl(context, food, sauce, price):
    module = f"foods.{food.lower()}"
    food = getattr(eval(module), food.title())(sauce, int(price))
    foods_.append(food)


@step("Mister Patate's favorite drink (Coca-Cola)")
def step_impl(context):
    context.drink = "Coca-Cola"


@when("Mister Patate add food in his formula")
def step_impl(context):
    context.formula = Formula(context.drink, foods_)


@then("he should have a list with all his favorite foods")
def step_impl(context):
    assert context.formula.drink == "Coca-Cola"
    assert len(context.formula.foods) == len(foods_)
