# -*- coding: utf-8 -*-

from __future__ import annotations

import logging
from typing import Union

from cars.motor import Motor

logger = logging.getLogger(__name__)


class Car:
    def __init__(self, current_speed: int = 0, horse_power: int = 0) -> None:
        assert current_speed >= 0, "The current speed have to be higher than 0"
        assert horse_power >= 0, "The horse power have to be higher than 0"
        # Indique la vitesse courante à un instant donné
        self._current_speed: int = current_speed
        # Indique le nombre de chevaux associé à la voiture
        self._horse_power: int = horse_power
        # Une voiture à un moteur
        self._motor: Motor = Motor(self._horse_power)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Car):
            logger.warning(
                f"{type(o).__name__} isn't type 'Car'. So, will use default __eq__"
            )
            return super().__eq__(o)
        return (
            self._motor == o._motor
            and self._current_speed == o._current_speed
            and self._horse_power == o._horse_power
        )

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"Car(current_speed={self._current_speed}, horse_power={self._horse_power}, motor={self._motor})"

    @property
    def current_speed(self) -> int:
        """Get the current speed

        :return: the current speed
        """
        return self._current_speed

    @property
    def horse_power(self) -> int:
        """Get the horsepower of the car

        :return:horse power
        """
        return self._horse_power

    @property
    def motor(self) -> Motor:
        """Get the motor installed in the car

        :return: Motor
        """
        return self._motor

    @horse_power.setter
    def horse_power(self, new_horse_power):
        assert new_horse_power >= 0
        self._horse_power = new_horse_power
        self._motor = Motor(new_horse_power)

    @current_speed.setter
    def current_speed(self, new_current_speed):
        assert new_current_speed >= 0
        self._current_speed = new_current_speed

    def improve(self, current_speed: int, horse_power: int) -> Car:
        """Improve the parameters of the cars

        :param current_speed: current speed
        :param horse_power:  horse power
        :return: object Car
        """
        assert current_speed >= self._current_speed, "The new speed have to be higher"
        assert horse_power >= self._horse_power, "The new horse power have to be higher"
        self.current_speed = current_speed
        self.horse_power = horse_power
        return self
