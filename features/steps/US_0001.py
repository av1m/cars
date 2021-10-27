from behave import *

from cars.car import Car

use_step_matcher("parse")


@given("Benjamin initialise his car with parameters {max_speed}, {horsepower}")
def step_impl(context, max_speed, horsepower):
    """
    :type context: behave.runner.Context
    :type max_speed: str
    :type horsepower: str
    """
    context.car = Car(max_speed=int(max_speed), horsepower=int(horsepower))


@when("Benjamin asked information about his car")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.info = context.car.__repr__()


@then("information's car are displayed on screen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if hasattr(context, "info"):
        pass
