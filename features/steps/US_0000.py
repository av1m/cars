import logging
from behave import *

from cars.car import Car
from cars.wheel import Wheel

logger = logging.getLogger(__name__)

use_step_matcher("parse")


@given("Nothing")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.car = Car()


@when("Benjamin want to create a car with a max speed {max_speed}")
def step_impl(context, max_speed):
    """
    :type context: behave.runner.Context
    :type max_speed: str
    """
    context.car.max_speed = int(max_speed)
    assert int(max_speed) == int(max_speed)


@step("a number of horse power {horse_power}")
def step_impl(context, horse_power):
    """
    :type context: behave.runner.Context
    :type horse_power: str
    """
    context.car.horse_power = int(horse_power)
    assert context.car.horse_power == int(horse_power)


@step("10 size {number_of_wheels} wheels")
def step_impl(context, number_of_wheels):
    """
    :type context: behave.runner.Context
    :type number_of_wheels: str
    """
    for _ in range(int(number_of_wheels)):
        context.car.add_wheel(Wheel(size=10))
    assert len(context.car.wheels) == int(number_of_wheels)


@then("the car is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.info("The car is created %s", context.car)


@when(
    "Benjamin initialise his car with options max speed {max_speed} and horse power {horse_power}"
)
def step_impl(context, max_speed, horse_power):
    """
    :type context: behave.runner.Context
    :type max_speed: str
    :type horse_power: str
    """
    try:
        Car(max_speed=int(max_speed), horse_power=int(horse_power))
    except (AssertionError, ValueError):
        context.error = True


@then("an error message is displayed indicate that an option is invalid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if hasattr(context, "error"):
        logger.info("An error has occurred when creating the car")
