# coding: utf-8
import logging

from behave import *

from cars.car import Car
from cars.wheel import Wheel

logger = logging.getLogger(__name__)
use_step_matcher("parse")


@given("Two cars already built")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.car1 = Car(
        max_speed=100, horsepower=150, wheels=[Wheel(size=20)] * 4, color="#FEFEFE"
    )
    context.car2 = Car(
        max_speed=200, horsepower=250, wheels=[Wheel(size=20)] * 4, color="#FEFEFE"
    )


@when("Kevin compares the two cars")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.compare = context.car1.__lt__(context.car2)


@then("The system displays the fastest car")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.compare is True
    logger.info("The fastest car is: %s", context.car2)
