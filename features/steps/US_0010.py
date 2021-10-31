# coding: utf-8

import logging

from behave import *

from cars.car import Car
from cars.wheel import Wheel

logger = logging.getLogger(__name__)
use_step_matcher("parse")


@given("An existing car")
def step_impl(context):
    context.car = Car(max_speed=19, horsepower=200)
    context.wheel = Wheel(size=55, has_rim=True)


@when("Thierry adds wheels to this car")
def step_impl(context):
    context.car.add_wheel(context.wheel)


@then("The wheel appears in the car")
def step_impl(context):
    assert context.wheel in context.car.wheels


@step("The car is associated with the wheel")
def step_impl(context):
    assert context.wheel.car == context.car


@when("Thierry associate a car to a wheel")
def step_impl(context):
    context.wheel.car = context.car
