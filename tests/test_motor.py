# -*- coding: utf-8 -*-

import unittest

from cars.motor import Motor, TypeMotor


class TestMotor(unittest.TestCase):
    def test_empty(self) -> None:
        motor: Motor = Motor(horse_power=0)
        self.assertEqual(motor.type_motor, TypeMotor.EMPTY)

    def test_raise(self) -> None:
        self.assertRaises(AssertionError, lambda: Motor(horse_power=-1))
        self.assertRaises(AssertionError, lambda: Motor(horse_power=None))  # type: ignore
        self.assertRaises(AssertionError, lambda: Motor(horse_power="1"))  # type: ignore

    def test_interval(self) -> None:
        self.assertEqual(Motor(horse_power=50).type_motor, TypeMotor.CITY)
        self.assertEqual(Motor(horse_power=150).type_motor, TypeMotor.SPORT)
        self.assertEqual(Motor(horse_power=250).type_motor, TypeMotor.RACING)
        self.assertEqual(Motor(horse_power=350).type_motor, TypeMotor.F1)

    def test_all(self) -> None:
        all_type_motor: list[tuple[TypeMotor, int]] = [
            (TypeMotor.EMPTY, 0),
            (TypeMotor.CITY, 1),
            (TypeMotor.SPORT, 100),
            (TypeMotor.RACING, 200),
            (TypeMotor.F1, 300),
        ]

        type_motor: tuple[TypeMotor, int]
        for type_motor in all_type_motor:
            motor: Motor = Motor(horse_power=type_motor[1])
            self.assertEqual(motor.type_motor, type_motor[0])


if __name__ == "__main__":
    unittest.main()
