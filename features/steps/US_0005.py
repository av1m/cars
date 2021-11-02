# coding: utf-8
import logging

from behave import *

from cars.car import Car

logger = logging.getLogger(__name__)
use_step_matcher("parse")


@given("A Car")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.car = Car()


@when("Benjamin adds a {color}")
def step_impl(context, color: str):
    """
    :type context: behave.runner.Context
    :type color: str
    """
    try:
        context.car.color = color
    except AssertionError as e:
        context.exception = e


@then("the car has the requested color")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.info(f"The new car color {context.car.color}")


@then("a message indicates that the color is wrong")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if hasattr(context, "exception"):
        logger.info("The car has the wrong color")
    else:
        raise RuntimeError("The car should have the wrong color")
