# -*- coding: utf-8 -*-

"""
Representation of a Pizza
"""

import logging

from cars.truck import TruckFood
from foods.kebab import Kebab

logger = logging.getLogger(__name__)


class Pizza(Kebab):
    """Representation of a Pizza food"""

    pass


class TruckPizza(TruckFood):
    """Representation of a TruckPizza"""

    food = Pizza
