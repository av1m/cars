# -*- coding: utf-8 -*-

import unittest

from cars.car import Car
from cars.motor import Motor, TypeMotor
from cars.wheel import Wheel


class TestCar(unittest.TestCase):
    def test_default(self):
        car = Car()
        self.assertEqual(car.horse_power, 0)
        self.assertEqual(car.max_speed, 0)
        self.assertEqual(car.motor, Motor(0))
        self.assertEqual(car.wheels, tuple())

    def test_simple(self):
        car: Car = Car(
            max_speed=99, horse_power=100, wheels=[Wheel(size=5, has_rim=False)] * 4
        )
        self.assertEqual(car.horse_power, 100)
        self.assertEqual(car.max_speed, 99)
        self.assertEqual(car.motor, Motor(car.horse_power))
        self.assertEqual(car.motor.type_motor, TypeMotor.SPORT)
        self.assertIsInstance(car.wheels, tuple)
        for wheel in car.wheels:
            self.assertEqual(wheel, Wheel(size=5, has_rim=False))

    def test_raise(self):
        self.assertRaises(AssertionError, lambda: Car(max_speed=-1))
        self.assertRaises(AssertionError, lambda: Car(horse_power=-1))
        self.assertRaises(AssertionError, lambda: Car(wheels=Wheel()))  # type: ignore


if __name__ == "__main__":
    unittest.main()
