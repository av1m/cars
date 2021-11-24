# -*- coding: utf-8 -*-

"""
Representation of a Kebab
"""

import logging

from cars.truck import TruckFood
from foods.food import Food

logger = logging.getLogger(__name__)


class Kebab(Food):
    """Representation of a Kebab"""

    def __init__(self, sauce: str, price: int):
        self.sauce: str = sauce
        self.price: int = price

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(sauce='{self.sauce}', price={self.price})"

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__} with sauce {self.sauce} and price {self.price}"
        )

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, type(self)):
            logger.warning(
                "%s isn't type '%s'. So, will use default __eq__",
                type(o).__name__,
                self.__class__.__name__,
            )
            return super().__eq__(o)
        return self.sauce == o.sauce and self.price == o.price

    def __hash__(self):
        return hash((self.sauce, self.price))

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, price: int) -> None:
        """Setter for price

        :param price: The price to set
        :type price: int
        """
        if price < 0:
            raise ValueError("Price can't be negative")
        self._price = price


class TruckKebab(TruckFood):
    food = Kebab
