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


@when("Benjamin wants to create a car with a max speed {max_speed}")
def step_impl(context, max_speed):
    """
    :type context: behave.runner.Context
    :type max_speed: str
    """
    context.car.max_speed = int(max_speed)


@step("a number of horsepower {horsepower}")
def step_impl(context, horsepower):
    """
    :type context: behave.runner.Context
    :type horsepower: str
    """
    context.car.horsepower = int(horsepower)


@step("10 size {number_of_wheels} wheels")
def step_impl(context, number_of_wheels):
    """
    :type context: behave.runner.Context
    :type number_of_wheels: str
    """
    for _ in range(int(number_of_wheels)):
        context.car.add_wheel(Wheel(size=10))


@then("the car is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.info("The car is created %s", context.car)


@when(
    "Benjamin initialise his car with options max speed {max_speed} and horsepower {horsepower}"
)
def step_impl(context, max_speed, horsepower):
    """
    :type context: behave.runner.Context
    :type max_speed: str
    :type horsepower: str
    """
    try:
        Car(max_speed=int(max_speed), horsepower=int(horsepower))
    except (AssertionError, ValueError):
        context.error = True


@then("an error message is displayed indicate that an option is invalid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if hasattr(context, "error"):
        logger.info("An error has occurred when creating the car")
