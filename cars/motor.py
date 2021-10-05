# -*- coding: utf-8 -*

from __future__ import annotations

import logging
from enum import Enum

logger = logging.getLogger(__name__)


class TypeMotor(Enum):
    EMPTY = 0
    CITY = 1
    SPORT = 100
    RACING = 200
    F1 = 300


class Motor:
    def __init__(self, horse_power):
        self.__type = Motor.get_type(horse_power)

    @property
    def type(self) -> TypeMotor:
        return self.__type

    @staticmethod
    def get_type(horse_power) -> TypeMotor:
        """Attribue le type en fonction du nombre de chevaux

        1. Récupère la liste des types de moteurs
        2. L'attribution du type est fait en fonction du plus petit nombre le plus proche des valeurs de TypeMotor

        :param horse_power:
        :return: TypeMotor
        """
        # Get all TypeMotor values (e.g. [0, 1, 100, 200, 300])
        typemotor_values = list(TypeMotor._value2member_map_.keys())
        # Sort the list in reverse mode
        typemotor_values.sort(reverse=True)
        # Get the smallest closest value
        type = min(typemotor_values, key=lambda v: v - horse_power > 0)

        return TypeMotor(type)

    def __str__(self):
        return self.__repr__()

    def __repr__(self) -> str:
        return f"Motor(type={self.__type})"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Motor):
            logger.warning(
                f"{type(o).__name__} isn't type 'Motor'. So, will use default __eq__"
            )
            return super().__eq__(o)
        return self.type == o.type
