# -*- coding: utf-8 -*
"""
Representation of an motor and type of mottor for a car
"""

from __future__ import annotations

import logging
from enum import Enum
from functools import total_ordering

logger = logging.getLogger(__name__)


@total_ordering
class TypeMotor(Enum):
    """Enumeration of the type of motor

    The values associated with the enumeration elements correspond
    to the minimum value of the associated interval the power in horses of a vehicle
    In other words, it's the minimal threshold of power in the horse of the car
    """

    EMPTY = 0  # No motor
    CITY = 1
    SPORT = 100
    RACING = 200
    F1 = 300

    def __next__(self) -> TypeMotor:
        """Get the next value of the enumeration

        If the current value is the last one, it returns the last one
        This method never raises an exception

        :return: the next value of the enumeration
        :rtype: TypeMotor
        """
        members: list[TypeMotor] = list(self.__class__)
        index: int = members.index(self) + 1
        if index >= len(members):
            index = len(members) - 1
        return members[index]

    def __iter__(self) -> TypeMotor:
        """Iterate over the enum values

        This function return the current instance
        The next function is used here to get the next value of the enumeration

        :return: An iterator over the enum values
        :rtype: TypeMotor
        """
        return self

    def __lt__(self, other: TypeMotor) -> bool:
        """Compare the current value with another value

        :param other: The other value to compare with
        :type other: TypeMotor
        :return: True if the current value is lower than the other value
        :rtype: bool
        """
        return self.value < other.value

    @staticmethod
    def get_all() -> dict[str, int]:
        """Get all enum keys and values

        Exemple::

            >>> TypeMotor.dict()
            >>> {"EMPTY": 0, "CITY": 1, "SPORT": 100, "RACING": 200, "F1": 300}

        :return: A dictionary or keys are the names of Enums and Values are the associated values
        :rtype: dict[str, int]
        """
        return {t.name: t.value for t in TypeMotor}


@total_ordering
class Motor:
    """Representation of an motor

    A motor is associated with a car and have a type of motor
    The type of motor should not be changed after the creation of the motor
    """

    def __init__(self, horsepower: int) -> None:
        """Constructor method

        :param horsepower: the horsepower of the motor
        :type horsepower: int
        """
        assert isinstance(horsepower, int), "horsepower must be an integer"
        assert horsepower >= 0, "The horsepower must be positive"
        # Allow to make the type immutable
        self.type = Motor.compute_type(horsepower)
        return

    def __str__(self) -> str:
        return f"Motor {self.type_motor.name}"

    def __repr__(self) -> str:
        return f"Motor(type={self.type_motor})"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Motor):
            logger.warning(
                "%s isn't type 'Motor'. So, will use default __eq__", type(o).__name__
            )
            return super().__eq__(o)
        return self.type_motor == o.type_motor

    def __hash__(self):
        return hash(self.type_motor)

    def __lt__(self, other: Motor) -> bool:
        """Compare the current motor with another value (motor)

        :param other: The other value to compare with
        :type other: Motor
        :return: True if the current value is lower than the other value
        :rtype: bool
        """
        if not isinstance(other, Motor):
            logger.warning(
                "%s isn't type 'Motor'. So, will use default __lt__",
                type(other).__name__,
            )
            return super().__lt__(other)
        return self.type_motor < other.type_motor

    @property
    def type_motor(self) -> TypeMotor:
        """Getter of the type of motor

        :return: The type of motor associated with a horsepower
        :rtype: TypeMotor
        """
        return self.type

    @staticmethod
    def compute_type(horsepower: int) -> TypeMotor:
        """Assigns the type according to the number of horses

        1. Retrieves the list of motors types
        2. Type attribution is based on the smallest number closest to TypeMotor values

        :param horsepower: Power of the car
        :type horsepower: int
        :return: The type of motor associated with the power of the car
        :rtype: TypeMotor
        """
        assert horsepower >= 0, "The horsepower of the car must be greater than 0"
        # Get all TypeMotor values (e.g. [0, 1, 100, 200, 300]) with reverse sorted (descending)
        type_motor_list: list[int] = sorted(TypeMotor.get_all().values(), reverse=True)
        # Get the smallest closest value
        type_motor: int = min(type_motor_list, key=lambda v: v - horsepower > 0)
        return TypeMotor(type_motor)
