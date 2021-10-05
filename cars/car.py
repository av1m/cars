# -*- coding: utf-8 -*-
"""
Representation of Car, also called Vehicle
"""

from __future__ import annotations

import copy
import logging

from cars.motor import Motor
from cars.wheel import Wheel

logger = logging.getLogger(__name__)


class Car:
    """Representation of a car

    Exemple::

        car: Car = Car(max_speed=220, horse_power=120)
        print(car)
    """

    def __init__(
        self, max_speed: int = 0, horse_power: int = 0, wheels: list[Wheel] = []
    ) -> None:
        """Constructor method

        :param max_speed: maximum speed of the car
        :type max_speed: int
        :param horse_power: number of horses associated with the car
        :type horse_power: int
        :param wheels: list of wheels associated to the car
        :type wheels: list[Wheel]
        """
        self.max_speed: int = max_speed
        self.horse_power: int = horse_power
        # A car have only one motor
        self._motor: Motor = Motor(self._horse_power)
        self._wheels: list[Wheel] = copy.deepcopy(wheels)
        return

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Car):
            logger.warning(
                f"{type(o).__name__} isn't type 'Car'. So, will use default __eq__"
            )
            return super().__eq__(o)
        return (
            self.motor == o.motor
            and self.max_speed == o.max_speed
            and self.horse_power == o.horse_power
        )

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"Car(max_speed={self.max_speed}, horse_power={self.horse_power}, motor={self.motor})"

    @property
    def wheels(self) -> tuple[Wheel, ...]:
        """Getter method for wheels

        :return: the wheels of the car
        :rtype: tuple[Wheel]
        """
        return tuple(self._wheels)

    def add_wheel(self, wheel: Wheel) -> tuple[Wheel, ...]:
        """Add a new wheel to the car

        :param wheel: the new wheel to add to the car
        :type wheel: Wheel
        :return: the list of wheels associated with the current car and the new wheel
        :rtype: tuple[Wheel, ...]
        """
        assert isinstance(wheel, Wheel), "attribute wheel must have type 'Wheel'"
        self._wheels.append(wheel)
        return self.wheels

    @property
    def max_speed(self) -> int:
        """Getter of max_speed attributes

        :return: The maximum speed of the car
        :rtype: int
        """
        return self._max_speed

    @max_speed.setter
    def max_speed(self, new_max_speed: int) -> None:
        """Setter for maximum speed of the car

        We check that new maximum speed is an integer and that it is higher than 0
        This method modifies the instance of the class
        """
        assert isinstance(new_max_speed, int), "The maximum speed must be an integer"
        assert new_max_speed >= 0, "The max speed have to be higher than 0"
        self._max_speed = new_max_speed
        return

    @property
    def horse_power(self) -> int:
        """Getter of horse_power attributes

        :return: The number of horses power associated with the car
        :rtype: int
        """
        return self._horse_power

    @horse_power.setter
    def horse_power(self, new_horse_power: int) -> None:
        """Setter of horse_power attributes

        We check that new_horse_power is an integer and that it is higher than 0
        This method modifies the instance of the class and changes the motor of the car
        """
        assert isinstance(new_horse_power, int), "The horse power must be an integer"
        assert new_horse_power >= 0, "The horse power have to be higher than 0"
        self._horse_power = new_horse_power
        self._motor = Motor(new_horse_power)
        logging.debug(f"From {new_horse_power} horse powers, the motor is {self.motor}")
        return

    @property
    def motor(self) -> Motor:
        """Getter of the motor installed in the car

        :return: the motor installed in the car
        :rtype: Motor
        """
        return self._motor

    def improve(self, new_max_speed: int, new_horse_power: int) -> Car:
        """Improve the parameters of the cars

        Allows upgrade the car by passing a new speed and a new number of horses
        This method modifies the instance of the class and changes the motor of the car

        :param new_max_speed: The new maximum speed of the car
        :type new_max_speed: int
        :param new_horse_power: The new horse power of the car and that allows to assign the engine of the car
        :type new_horse_power: int
        :return: the current instance modified of Car
        :rtype: Car
        """
        assert new_max_speed >= self.max_speed, "The new speed have to be higher"
        assert (
            new_horse_power >= self.horse_power
        ), "The new horse power have to be higher"
        self.max_speed = new_max_speed
        self.horse_power = new_horse_power
        return self
