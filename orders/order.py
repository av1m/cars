# coding: utf-8
from datetime import datetime
from typing import Sequence

from cars.car import Car
from foods.formula import Formula


class Order:
    def __init__(
        self,
        order_id: str,
        car: Car,
        formulas: Sequence[Formula] = None,
        date: datetime = datetime.now(),
    ):
        if not formulas:
            formulas = []
        assert isinstance(order_id, str), "order_id must be str"
        assert isinstance(car, Car), "car must be a Car"
        assert isinstance(formulas, Sequence), "formulas must be a Sequence"
        assert isinstance(date, datetime), "date must be a datetime"
        self.order_id: str = order_id
        self.car: Car = car
        self.formulas: Sequence[Formula] = formulas
        self.date: datetime = date
