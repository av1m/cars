# -*- coding: utf-8 -*-

from __future__ import annotations

import abc
import inspect
from typing import Iterable, Optional, Sequence, Type, final

from cars.car import Car
from foods.food import Food
from foods.formula import Formula


class TruckFood(Car, metaclass=abc.ABCMeta):
    """Class that represent a car food
    This class is an abstract base class
    This class is a subclass of Car

    A TruckFood has
    - a food specialty which is the "Food" which inherits (see __init_subclass__)
    - a predefined menu that corresponds to a set of Formula

    So a customer buys a formula.
    """

    food: Type[Food]

    def __init__(self, formulas: Iterable[Formula], *args, **kwargs) -> None:
        """Initialize the instance of the class

        :param formulas: the formulas
        :type formulas: Iterable[Formula]
        :param args: the arguments
        :type args: Iterable
        :param kwargs: the keyword arguments
        :type kwargs: dict
        """
        self._formulas: dict[int, Formula] = {i: f for i, f in enumerate(formulas, 1)}
        self._orders: list[int] = []
        super().__init__(*args, **kwargs)

    def __init_subclass__(cls, *args, **kwargs) -> None:
        """Initialize the subclass of the class
        Verify that the food is supported

        :param args: the arguments
        :type args: Sequence
        :param kwargs: the keyword arguments
        :type kwargs: dict
        """
        if not (inspect.isclass(cls.food) and issubclass(cls.food, Food)):
            raise AttributeError(
                "The class must have a food attribute that is a subclass of Food"
            )
        # https://github.com/python/mypy/issues/4660
        super().__init_subclass__(*args, **kwargs)  # type: ignore

    def __str__(self) -> str:
        return super().__str__() + f" and can sell {self.food.__name__}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.formulas!r})"

    @property
    @final
    def formulas(self) -> dict[int, Formula]:
        """Return the formulas of the truck
        This property is final

        :return: the formulas
        :rtype: dict[int, Formula]
        """
        return self._formulas

    @property
    @final
    def orders(self) -> Sequence[int]:
        """Return the orders of the truck

        :return: the orders
        :rtype: Sequence[int]
        """
        return tuple(self._orders)

    @final
    def add_order(self, formula: int) -> Optional[Formula]:
        """Add an order to the truck

        :param formula: the number of the formula
        :type formula: int
        :return: the formula
        :rtype: Formula
        """
        if formula not in self.formulas:
            raise ValueError(
                f"The formula {formula} does not exist, please check orders property"
            )
        self._orders.append(formula)
        return self.formulas.get(formula)

    @final
    def undo_last_order(self) -> Optional[tuple[int, Formula]]:
        """Undo the last order

        :return: the number of the formula and the formula
        :rtype: tuple[int, Formula]
        """
        # Pop the last item of orders and return it
        formula_number = self._orders.pop()
        formula = self.formulas.get(formula_number)
        return (formula_number, formula) if formula else None

    @staticmethod
    def from_food(food: Type[Food]) -> Type[TruckFood]:
        """Return the TruckFood subclass associated to the food

        :param food: the food
        :type food: Food
        :return: the TruckFood subclass of the food
        :rtype: TruckFood
        """
        for subclass in TruckFood.__subclasses__():
            if subclass.food is food:
                return subclass
        raise TypeError(f"The food {food.__name__} is not supported")
