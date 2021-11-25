# coding: utf-8

import logging

from behave import *

from foods.formula import Formula
from foods.kebab import Kebab, TruckKebab

logger = logging.getLogger(__name__)
use_step_matcher("parse")


@given("A kebab truck")
def step_impl(context):
    context.kebab_truck = TruckKebab(
        formulas=[Formula("Pepsi", [Kebab(sauce="Beef", price=14)])]
    )


@when("Edouard place an order")
def step_impl(context):
    context.kebab_truck.add_order(1)


@then("Edouard can see all his orders")
def step_impl(context):
    expected = (1,)
    for order in context.kebab_truck.orders:
        logger.info(context.kebab_truck.formulas.get(order))
        assert context.kebab_truck.orders == expected


@when("Edouard place a bad order")
def step_impl(context):
    try:
        context.kebab_truck.add_order(2)
    except ValueError as e:
        logger.info(
            "Cannot place the order with order = 2 because %s",
            getattr(e, "message", repr(e)),
        )
        context.exception = True


@given("A kebab truck with menu")
def step_impl(context):
    formulas = [
        Formula("Pepsi", [Kebab(sauce="Beef", price=14)] * 2),
        Formula("Orangina", [Kebab(sauce="Barbecue", price=10)]),
    ]
    context.kebab_truck = TruckKebab(formulas=formulas)


@when("Edouard ask for the menu")
def step_impl(context):
    context.menu = context.kebab_truck.formulas


@then("he should see the menu")
def step_impl(context):
    drinks = [formula.drink for formula in context.menu.values()]
    assert drinks == ["Pepsi", "Orangina"]
