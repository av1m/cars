import logging

from behave import *

from cars.car import Car
from cars.motor import TypeMotor
from cars.wheel import Wheel

logger = logging.getLogger(__name__)

use_step_matcher("parse")


@given("Benjamin had a racing car")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.racing_car = Car(horse_power=250)
    assert context.racing_car.motor.type_motor == TypeMotor.RACING


@when("he want to add {number_wheels} wheel of {wheel_size} size")
def step_impl(context, number_wheels, wheel_size):
    """
    :type context: behave.runner.Context
    :type number_wheels: str
    :type wheel_size: str
    """
    for _ in range(int(number_wheels)):
        context.racing_car.add_wheel(Wheel(size=int(wheel_size)))
    assert len(context.racing_car.wheels) == int(number_wheels)


@then("the system show us the newly wheels")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.info("All wheels of the racing car %", context.racing_car.wheels)
