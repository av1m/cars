# coding: utf-8

import logging
from foods.formula import Formula

logger = logging.getLogger(__name__)


class Kebab:
    def __init__(self, sauce: str, price: int):
        self.sauce = sauce
        self.price = price

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Kebab):
            logger.warning(
                "%s isn't type 'Kebab'. So, will use default __eq__", type(o).__name__
            )
            return super().__eq__(o)
        return self.sauce == o.sauce and self.price == o.price
