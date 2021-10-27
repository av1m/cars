# coding: utf-8
import logging

from behave import *

from cars.car import Car
from cars.wheel import Wheel

logger = logging.getLogger(__name__)
use_step_matcher("parse")


@given("A car already built")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.good_car = Car(
        max_speed=100, horsepower=100, wheels=[Wheel(size=20)] * 4, color="#FEFEFE"
    )
    context.wrong_car = Car(
        max_speed=100, horsepower=1000, wheels=[Wheel(size=20)] * 4, color="#FEFEFE"
    )


@when("Tony checks if the motor is compliant")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.is_compliant = context.good_car.is_conform()
    context.is_not_compliant = context.wrong_car.is_conform()


@then("The system indicates the compliance")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.is_compliant is True
    logger.info("The car is compliant")


@then("The system indicates an error")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if hasattr(context, "is_not_compliant"):
        assert context.is_not_compliant is False
    logger.info("The car is not compliant")
