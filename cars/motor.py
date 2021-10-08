# -*- coding: utf-8 -*
"""
Representation of an motor and type of mottor for a car
"""

from __future__ import annotations

import logging
from enum import Enum

logger = logging.getLogger(__name__)


class TypeMotor(Enum):
    """Enumeration of the type of motor

    The values associated with the enumeration elements correspond to the minimum value of the associated interval the power in horses of a vehicle
    In other words, it's the minimal threshold of power in the horse of the car
    """

    EMPTY = 0  # No motor
    CITY = 1
    SPORT = 100
    RACING = 200
    F1 = 300

    @staticmethod
    def dict() -> dict[str, int]:
        """Get all enum keys and values

        Exemple::

            >>> TypeMotor.dict()
            >>> {"EMPTY": 0, "CITY": 1, "SPORT": 100, "RACING": 200, "F1": 300}

        :return: A dictionary or keys are the names of Enums and Values are the associated values
        :rtype: dict[str, int]
        """
        return {t.name: t.value for t in TypeMotor}


class Motor:
    """Representation of an motor

    A motor is associated with a car and have a type of motor
    The type of motor can't be changed after the creation of the motor
    """

    def __init__(self, horse_power: int) -> None:
        """Constructor method

        :param horse_power: the horse power of the motor
        :type horse_power: int
        """
        assert isinstance(horse_power, int), "horse_power must be an integer"
        assert horse_power >= 0, "The horse power must be positive"
        # Allow to make the type immutable
        self.__type = Motor.compute_type(horse_power)
        return

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"Motor(type={self.type_motor})"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Motor):
            logger.warning(
                f"{type(o).__name__} isn't type 'Motor'. So, will use default __eq__"
            )
            return super().__eq__(o)
        return self.type_motor == o.type_motor

    @property
    def type_motor(self) -> TypeMotor:
        """Getter of the type of motor

        :return: The type of motor associated with a horse power
        :rtype: TypeMotor
        """
        return self.__type

    @staticmethod
    def compute_type(horse_power: int) -> TypeMotor:
        """Assigns the type according to the number of horses

        1. Retrieves the list of motors types
        2. Type attribution is based on the smallest number closest to TypeMotor values

        :param horse_power: Power of the car
        :type horse_power: int
        :return: The type of motor associated with the power of the car
        :rtype: TypeMotor
        """
        assert horse_power >= 0, "The horse power of the car must be greater than 0"
        # Get all TypeMotor values (e.g. [0, 1, 100, 200, 300]) with reverse sorted (descending)
        type_motor_list: list[int] = sorted(TypeMotor.dict().values(), reverse=True)
        # Get the smallest closest value
        type_motor: int = min(type_motor_list, key=lambda v: v - horse_power > 0)
        return TypeMotor(type_motor)
