# -*- coding: utf-8 -*-
"""
Representation of a Food
"""

from __future__ import annotations

import abc
import inspect
from typing import Type

import cars


class Food(abc.ABC):
    """Representation of a Food
    This class is an abstract base class.
    """

    @abc.abstractmethod
    def __eq__(self, other):
        pass

    @abc.abstractmethod
    def __hash__(self):
        pass

    @property
    @abc.abstractmethod
    def price(self) -> int:
        """Return the price of the food

        :return: The price of the food
        :rtype: int
        """
        pass

    @classmethod
    def get_truck(cls) -> Type[cars.TruckFood]:
        """Return the truck food class
        This method is used to get the truck food class associated with this food.

        cls needs to be a subclass of Food

        :return: The truck food class associated with this food
        :rtype: Type[cars.TruckFood]
        """
        # Check if cls is an abstract class
        if inspect.isabstract(cls):
            raise TypeError("Can't create cars.TruckFood from abstract class")
        return cars.TruckFood.from_food(cls)

    @classmethod
    def create_truck(cls, *args, **kwargs) -> cars.TruckFood:
        """Return the truck food associated with this food
                This method is used to create the truck food associated with this food.

                cls needs to be a subclass of Food

                This method does not ask for the iterable of formulas.
                But formulas is required for the creation of truck food.
                If formulas is not provided, a TypeError will raise (from __new__).
        x
                :return: The truck food associated with this food
                :rtype: cars.TruckFood
        """
        if inspect.isabstract(cls):
            raise TypeError("Can't create cars.TruckFood from abstract class")
        x = cars.TruckFood.from_food(cls)
        print(x)
        return x(*args, **kwargs)
