# coding: utf-8
import logging

from behave import *

from cars.car import Car

logger = logging.getLogger(__name__)
use_step_matcher("parse")


@given("A car already built with a weight")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.car = Car(weight=1000)


@given("Benjamin create a car with a {weight}")
def step_impl(context, weight):
    """
    :type context: behave.runner.Context
    :type weight: str
    """
    try:
        context.car = Car(weight=int(weight))
    except (AssertionError, ValueError) as e:
        logger.info(
            "Cannot create the car with weight = %s because %s",
            weight,
            getattr(e, "message", repr(e)),
        )
        context.exception = True


@when("Benjamin change the {weight} to his car")
def step_impl(context, weight):
    """
    :type context: behave.runner.Context
    :type weight: str
    """
    try:
        context.car.weight = int(weight)
    except (AssertionError, ValueError, AttributeError):
        context.exception = True
        logger.info("Cannot create the car with weight = %s", weight)


@then("the {weight} of the car is increased")
def step_impl(context, weight):
    """
    :type context: behave.runner.Context
    :type weight: str
    """
    assert context.car.weight == int(weight)
