# -*- coding: utf-8 -*-
"""
Representation of Car, also called Vehicle
"""

from __future__ import annotations

import copy
import logging
import re
from functools import total_ordering
from typing import Optional

from cars.motor import Motor, TypeMotor
from cars.wheel import Wheel

logger = logging.getLogger(__name__)


@total_ordering
class Car:
    """Representation of a car

    Exemple::

        car: Car = Car(max_speed=220, horsepower=120)
        print(car)
    """

    def __init__(
        self,
        max_speed: int = 0,
        horsepower: int = 0,
        color: str = "#FFFFFF",
        weight: int = 0,
        wheels: Optional[list[Wheel]] = None,
    ) -> None:
        """Constructor method

        :param max_speed: maximum speed of the car in km/h
        :type max_speed: int
        :param horsepower: number of horses associated with the car
        :type horsepower: int
        :param color: the color of the car. must be in hexadecimal format and preceded by a "#"
        :type color: str
        :param weight: the weight of the car in kg
        :type weight: int
        :param wheels: list of wheels associated to the car
        :type wheels: list[Wheel]
        """
        if wheels is None:
            wheels = []
        else:
            assert isinstance(wheels, list), "wheels need to be a list of Wheel"
        self.max_speed: int = max_speed
        self.horsepower: int = horsepower
        self.weight: int = weight
        self.color: str = color
        # A car have only one motor
        self._motor: Motor = Motor(self.horsepower)
        # By default, we don't have wheels
        self._wheels: list[Wheel] = []
        for wheel in wheels:
            self.add_wheel(copy.deepcopy(wheel))
        return

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Car):
            logger.warning(
                "%s isn't type 'Car'. So, will use default __eq__", type(o).__name__
            )
            return super().__eq__(o)
        return (
            self.motor == o.motor
            and self.max_speed == o.max_speed
            and self.horsepower == o.horsepower
            and self.color == o.color
        )

    def __hash__(self):
        return hash((self.motor, self.max_speed, self.horsepower, self.color))

    def __str__(self) -> str:
        return (
            f"This {self.__class__.__name__} at a maximum speed of {self.max_speed} km/h "
            f"using its {self.motor}, its {self.horsepower} hp "
            f"and its {len(self.wheels)} wheels"
        )

    def __lt__(self, other: Car) -> bool:
        """Compare the car to another car

        The comparison is made on this order:
        - Horsepower
        - Speed
        - Weight

        :return: True if the car is slower than the other car
        :rtype: bool
        """
        return (self.horsepower, self.max_speed, self.weight) < (
            other.horsepower,
            other.max_speed,
            other.weight,
        )

    def __repr__(self) -> str:
        return (
            f"Car(max_speed={self.max_speed}, "
            f"horsepower={self.horsepower}, "
            f"motor={self.motor}, "
            f"color={self.color})"
        )

    @property
    def wheels(self) -> tuple[Wheel, ...]:
        """Getter method for wheels

        :return: the wheels of the car
        :rtype: tuple[Wheel]
        """
        return tuple(self._wheels)

    @property
    def max_speed(self) -> int:
        """Getter of max_speed (in km/h) attributes

        :return: The maximum speed of the car
        :rtype: int
        """
        return self._max_speed

    @max_speed.setter
    def max_speed(self, new_max_speed: int) -> None:
        """Setter for maximum speed of the car

        The speed is represented in km/h

        We check that new maximum speed is an integer and that it is higher than 0
        This method modifies the instance of the class
        """
        assert isinstance(new_max_speed, int), "The maximum speed must be an integer"
        assert new_max_speed >= 0, "The max speed have to be higher than 0"
        self._max_speed = new_max_speed
        return

    @property
    def horsepower(self) -> int:
        """Getter of horsepower attributes

        :return: The number of horsepower associated with the car
        :rtype: int
        """
        return self._horsepower

    @horsepower.setter
    def horsepower(self, new_horsepower: int) -> None:
        """Setter of horsepower attributes

        We check that new_horsepower is an integer and that it is higher than 0
        This method modifies the instance of the class and changes the motor of the car

        :param new_horsepower: The new horsepower of the car
        :type new_horsepower: int
        """
        assert isinstance(new_horsepower, int), "The horsepower must be an integer"
        assert new_horsepower >= 0, "The horsepower have to be higher than 0"
        self._horsepower = new_horsepower
        self._motor = Motor(new_horsepower)
        logging.debug(
            "From %d horsepowers, the motor is %s", new_horsepower, self.motor
        )
        return

    @property
    def motor(self) -> Motor:
        """Getter of the motor installed in the car

        :return: the motor installed in the car
        :rtype: Motor
        """
        return self._motor

    @property
    def color(self) -> str:
        """Getter of the color installed in the car

        :return: the color installed in the car
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, new_color: str = "#FFFFFF") -> None:
        """Setter of color attributes

        This method modifies the instance of the class
        The color need to be a valid hexadecimal code color
        For example :
        - #FFFFFF
        - #40E0D0
        - #40E0D0

        :param new_color: The new color for the vehicle
        :type new_color: str
        :return: None
        """
        assert isinstance(new_color, str), "The color must be a string"
        assert re.compile("^#(?:[0-9a-fA-F]{3}){1,2}$").match(
            new_color
        ), "The color need to be a valid hexadecimal code"
        self._color = new_color.lower()

    @property
    def weight(self) -> int:
        """Getter of the weight of the car in kg

        :return: the weight of the car
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, new_weight: int) -> None:
        """Setter of weight attributes

        The weight need to be an integer and higher than 0
        This method modifies the instance of the class

        :param new_weight: The new weight of the car in kg
        :type new_weight: int
        :return: None
        """
        assert isinstance(new_weight, int), "The weight must be an integer"
        assert new_weight >= 0, "The weight have to be higher than 0"
        self._weight = new_weight
        return

    def add_wheel(self, wheel: Wheel) -> tuple[Wheel, ...]:
        """Add a new wheel to the car

        :param wheel: the new wheel to add to the car
        :type wheel: Wheel
        :return: the list of wheels associated with the current car and the new wheel
        :rtype: tuple[Wheel, ...]
        """
        assert isinstance(wheel, Wheel), "attribute wheel must have type 'Wheel'"
        if wheel.car is None:
            # It's the responsibility of the wheel property to add bidirectional access
            wheel.car = self
        return self.wheels

    def improve(self, new_max_speed: int, new_horsepower: int) -> Car:
        """Improve the parameters of the cars

        Allows upgrade the car by passing a new speed and a new number of horses
        This method modifies the instance of the class and changes the motor of the car

        :param new_max_speed: The new maximum speed of the car
        :type new_max_speed: int
        :param new_horsepower: New horsepower of the car and assign a new engine to the car
        :type new_horsepower: int
        :return: the current instance modified of Car
        :rtype: Car
        """
        assert new_max_speed >= self.max_speed, "The new speed have to be higher"
        assert new_horsepower >= self.horsepower, "The new horsepower have to be higher"
        self.max_speed = new_max_speed
        self.horsepower = new_horsepower
        return self

    def is_conform(self) -> bool:
        """Check if the motor and the maximum speed are conform

        This method verify the conformity in terms of :
        - Horsepower (motor)
        - Maximum speed

        If the max_speed is very large, we check against the largest motor we have
        In real life there are bigger motors,
        but here we are assuming that the bigger motors is the one generated by max (TypeMotor)

        :return: if the motor and the maximum speed are conform
        :rtype: bool
        """
        type_motor: TypeMotor = Motor(self.max_speed).type_motor
        return self.motor.type_motor == type_motor
