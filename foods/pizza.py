# -*- coding: utf-8 -*-

"""
Representation of a Pizza
"""

import logging

import cars
import foods

logger = logging.getLogger(__name__)


class Pizza(foods.Kebab):
    """Representation of a Pizza food"""

    pass


class TruckPizza(cars.TruckFood):
    """Representation of a TruckPizza"""

    food = Pizza
