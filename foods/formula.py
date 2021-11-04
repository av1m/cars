# -*- coding: utf-8 -*-

import logging

from foods.kebab import Kebab

logger = logging.getLogger(__name__)


class Formula:
    def __init__(self, drink: str, kebabs: list[Kebab]):
        self.drink = drink
        self.kebabs = kebabs

    @property
    def price(self) -> int:
        """Formula price is sum of all kebabs prices

        :return: Formula price
        :rtype: int
        """
        return sum([kebab.price for kebab in self.kebabs])

    def add_kebab(self, kebab: Kebab) -> list[Kebab]:
        """Add kebab to formula

        :param kebab: Kebab to add
        :type kebab: Kebab
        :return: list of kebabs
        :rtype: list[Kebab]
        """
        self.kebabs.append(kebab)
        return self.kebabs

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Formula):
            logger.warning(
                "%s isn't type 'Formula'. So, will use default __eq__", type(o).__name__
            )
            return super().__eq__(o)
        return (
            self.drink == o.drink and self.kebabs == o.kebabs and self.price == o.price
        )
