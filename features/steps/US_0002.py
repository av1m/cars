import logging

from behave import *

from cars.car import Car

logger = logging.getLogger(__name__)

use_step_matcher("parse")


@when("Benjamin asked to improve his car with {new_max_speed} and {new_horsepower}")
def step_impl(context, new_max_speed, new_horsepower):
    """
    :type context: behave.runner.Context
    :type new_max_speed: str
    :type new_horsepower: str
    """
    if not hasattr(context, "car"):
        context.car = Car()
    context.new_options = (new_max_speed, new_horsepower)
    context.car.improve(
        new_max_speed=int(new_max_speed), new_horsepower=int(new_horsepower)
    )


@then("his car characteristics have been modified")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    new_max_speed, new_horsepower = context.new_options
    assert context.car.max_speed == int(new_max_speed)
    assert context.car.horsepower == int(new_horsepower)


@given("Benjamin has already defined his car with {max_speed} and {horsepower}")
def step_impl(context, max_speed, horsepower):
    """
    :type context: behave.runner.Context
    :type max_speed: str
    :type horsepower: str
    """
    try:
        context.car2 = Car(max_speed=int(max_speed), horsepower=int(horsepower))
        assert context.car2.max_speed == int(max_speed)
        assert context.car2.horsepower == int(horsepower)
    except (AssertionError, ValueError):
        context.error2 = True


@when(
    "Benjamin asked to improve the characteristics up to {new_max_speed} and {new_horsepower}"
)
def step_impl(context, new_max_speed, new_horsepower):
    """
    :type context: behave.runner.Context
    :type new_max_speed: str
    :type new_horsepower: str
    """
    try:
        context.car2.improve(
            new_max_speed=int(new_max_speed), new_horsepower=int(new_horsepower)
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
