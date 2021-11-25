# coding: utf-8

import logging

from behave import *

from foods.formula import Formula
from foods.kebab import Kebab, TruckKebab

logger = logging.getLogger(__name__)
use_step_matcher("parse")


@given("An order placed in a kebab truck")
def step_impl(context):
    context.kebab_truck = TruckKebab(
        formulas=[Formula("Pepsi", [Kebab(sauce="Beef", price=14)])]
    )
    context.kebab_truck.add_order(1)


@when("Hatward undo the last order")
def step_impl(context):
    context.last_order = context.kebab_truck.undo_last_order()


@then("the order is cancelled")
def step_impl(context):
    assert context.last_order[0] == 1


@when("Hatward undo the last order that was not placed")
def step_impl(context):
    try:
        context.last_order = context.kebab_truck.undo_last_order()
    except IndexError:
        context.exception = True
