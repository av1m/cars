# -*- coding: utf-8 -*-

import unittest

from cars.motor import Motor, TypeMotor


class TestMotor(unittest.TestCase):
    def test_empty(self) -> None:
        motor: Motor = Motor(horse_power=0)
        self.assertEqual(motor.type_motor, TypeMotor.EMPTY)

    def test_compute(self) -> None:
        self.assertEqual(Motor.compute_type(horse_power=0), TypeMotor.EMPTY)
        self.assertEqual(Motor.compute_type(horse_power=50), TypeMotor.CITY)
        self.assertEqual(Motor.compute_type(horse_power=150), TypeMotor.SPORT)
        self.assertEqual(Motor.compute_type(horse_power=250), TypeMotor.RACING)
        self.assertEqual(Motor.compute_type(horse_power=350), TypeMotor.F1)

    def test_raise(self) -> None:
        self.assertRaises(AssertionError, lambda: Motor(horse_power=-1))
        self.assertRaises(AssertionError, lambda: Motor(horse_power=None))  # type: ignore
        self.assertRaises(AssertionError, lambda: Motor(horse_power="1"))  # type: ignore
        self.assertRaises(AssertionError, lambda: Motor.compute_type(horse_power=-1))  # type: ignore
        self.assertRaises(TypeError, lambda: Motor.compute_type(horse_power=None))  # type: ignore

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

    def test_equals(self) -> None:
        motor: Motor = Motor(horse_power=0)
        self.assertEqual(motor, Motor(0))
        motor = Motor(horse_power=150)
        self.assertEqual(motor, Motor(150))
        self.assertNotEqual(motor, Motor(900))


class TestTypeMotor(unittest.TestCase):
    def test_len(self) -> None:
        self.assertEqual(len(TypeMotor.get_all()), 5)

    def test_get_all(self) -> None:
        self.assertEqual(type(TypeMotor.get_all()), dict)
        self.assertTrue(all(str(x).isdigit() for x in TypeMotor.get_all().values()))
        self.assertTrue(all(str(x).isalnum() for x in TypeMotor.get_all().keys()))
        self.assertEqual(min(TypeMotor.get_all().values()), 0)
        self.assertEqual(max(TypeMotor.get_all().values()), 300)

    def test_equals(self) -> None:
        self.assertEqual(TypeMotor.EMPTY.value, 0)
        self.assertEqual(TypeMotor.CITY.value, 1)
        self.assertEqual(TypeMotor.SPORT.value, 100)
        self.assertEqual(TypeMotor.RACING.value, 200)
        self.assertEqual(TypeMotor.F1.value, 300)
        self.assertEqual(TypeMotor.get_all()["EMPTY"], 0)
        self.assertEqual(TypeMotor.get_all()["CITY"], 1)
        self.assertEqual(TypeMotor.get_all()["SPORT"], 100)
        self.assertEqual(TypeMotor.get_all()["RACING"], 200)
        self.assertEqual(TypeMotor.get_all()["F1"], 300)


if __name__ == "__main__":
    unittest.main()
