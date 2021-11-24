# coding: utf-8
import logging

from behave import *

from cars.car import Car
from cars.motor import TypeMotor

logger = logging.getLogger(__name__)
use_step_matcher("parse")


@given("An electric formula 1")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.formule1 = Car(horsepower=TypeMotor.RACING.value)


@when("Thierry improves the car so that it can go up to {kmh}")
def step_impl(context, kmh):
    """
    :type context: behave.runner.Context
    :type kmh: str
    """
    context.formule1.max_speed = int(kmh)


@then("Thierry can use an electric formula 1 climbed to its maximum speed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    logger.info(f"The car has a max speed of {context.formule1.max_speed}")
