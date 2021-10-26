import logging
from behave import *

from cars.car import Car

logger = logging.getLogger(__name__)

use_step_matcher("parse")


@when("Benjamin asked to improve his car with {new_max_speed} and {new_horse_power}")
def step_impl(context, new_max_speed, new_horse_power):
    """
    :type context: behave.runner.Context
    :type new_max_speed: str
    :type new_horse_power: str
    """
    if not hasattr(context, "car"):
        context.car = Car()
    context.new_options = (new_max_speed, new_horse_power)
    context.car.improve(
        new_max_speed=int(new_max_speed), new_horse_power=int(new_horse_power)
    )


@then("his car characteristics have been modified")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    new_max_speed, new_horse_power = context.new_options
    assert context.car.max_speed == int(new_max_speed)
    assert context.car.horse_power == int(new_horse_power)


@given("Benjamin has already defined his car with {max_speed} and {horse_power}")
def step_impl(context, max_speed, horse_power):
    """
    :type context: behave.runner.Context
    :type max_speed: str
    :type horse_power: str
    """
    try:
        context.car2 = Car(max_speed=int(max_speed), horse_power=int(horse_power))
        assert context.car2.max_speed == int(max_speed)
        assert context.car2.horse_power == int(horse_power)
    except (AssertionError, ValueError):
        context.error2 = True


@when(
    "Benjamin asked to improve the characteristics up to {new_max_speed} and {new_horse_power}"
)
def step_impl(context, new_max_speed, new_horse_power):
    """
    :type context: behave.runner.Context
    :type new_max_speed: str
    :type new_horse_power: str
    """
    try:
        context.car2.improve(
            new_max_speed=int(new_max_speed), new_horse_power=int(new_horse_power)
        )
    except (AssertionError, ValueError):
        context.error22 = True


@then("an error message is displayed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if hasattr("context", "error2") or hasattr("context", "error22"):
        logger.info("Can't improve the car")
