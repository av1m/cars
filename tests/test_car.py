# -*- coding: utf-8 -*-

import unittest

from cars.car import Car
from cars.motor import Motor


class CarTestCase(unittest.TestCase):
    def test_default(self):
        car = Car()
        self.assertEqual(car.horse_power, 0)
        self.assertEqual(car.current_speed, 0)
        self.assertEqual(car.motor, Motor(0))

    def test_getters(self):
        car = Car(current_speed=100, horse_power=150)
        self.assertEqual(car.horse_power, 100)
        self.assertEqual(car.current_speed, 150)

    def test_setters(self):
        car = Car(current_speed=100, horse_power=150)
        car.horse_power = 200
        self.assertEqual(car.horse_power, 200)
        self.assertEqual(car.current_speed, 100)
        car.current_speed = 120
        self.assertEqual(car.current_speed, 120)
        car.horse_power = -2
        car.current_speed = -2
        self.assertEqual(car.horse_power,200)
        self.assertEqual(car.current_speed, 120)


if __name__ == "__main__":
    unittest.main()
