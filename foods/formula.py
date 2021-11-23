# -*- coding: utf-8 -*-

import logging

from foods import Food

logger = logging.getLogger(__name__)


class Formula:
    """Formula class
    """

    def __init__(self, drink: str, foods: list[Food]):
        self.drink = drink
        self.foods = foods

    @property
    def price(self) -> int:
        """Formula price is sum of all foods prices

        :return: Formula price
        :rtype: int
        """
        return sum([food.price for food in self.foods])

    def add_food(self, food: Food) -> list[Food]:
        """Add food to formula

        :param food: Food to add
        :type food: Food
        :return: list of foods
        :rtype: list[Food]
        """
        self.foods.append(food)
        return self.foods

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Formula):
            logger.warning(
                "%s isn't type 'Formula'. So, will use default __eq__", type(o).__name__
            )
            return super().__eq__(o)
        return self.drink == o.drink and self.foods == o.foods and self.price == o.price

    def __str__(self) -> str:
        return f"For {self.price}$, you can drink {self.drink} and eats : {self.foods}"

    def __repr__(self) -> str:
        return f"Formula('{self.drink}', {self.foods})"
