from behave import *

from cars.motor import Motor

use_step_matcher("parse")


@given("Two motors already installed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.motor1 = Motor(100)
    context.motor2 = Motor(200)


@when("I compare the two motors")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.compare = context.motor1 < context.motor2


@then("I should see the motor with the best performance")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.compare is True
