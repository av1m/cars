# -*- coding: utf-8 -*-

import logging
from typing import Sequence

import foods

logger = logging.getLogger(__name__)


class Formula:
    """Formula class"""

    def __init__(self, drink: str, foods: Sequence[foods.Food] = None) -> None:
        self.drink = drink
        self.foods = set(foods) if foods else set()

    def __str__(self) -> str:
        return f"For {self.price}$, you can drink {self.drink} and eats : {self.foods}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.drink}', {self.foods})"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Formula):
            logger.warning(
                "%s isn't type %s. So, will use default __eq__",
                type(o).__name__,
                self.__class__.__name__,
            )
            return super().__eq__(o)
        return self.drink == o.drink and self.foods == o.foods and self.price == o.price

    def __hash__(self):
        return hash(self.drink) ^ hash(frozenset(self.foods))

    @property
    def price(self) -> int:
        """Formula price is sum of all foods prices

        :return: Formula price
        :rtype: int
        """
        return sum(food.price for food in self.foods)

    def add_food(self, food: foods.Food) -> Sequence[foods.Food]:
        """Add food to formula

        :param food: Food to add
        :type food: foods.Food
        :return: tuple of foods
        :rtype: Sequence[foods.Food]
        """
        self.foods.add(food)
        return tuple(self.foods)
