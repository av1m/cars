# -*- coding: utf-8 -*-

"""
Representation of a Pizza
"""

import logging

import foods

logger = logging.getLogger(__name__)


class Pizza(foods.Kebab):
    """Representation of a Pizza food"""

    pass


class TruckPizza(foods.TruckFood):
    """Representation of a TruckPizza"""

    food = Pizza
