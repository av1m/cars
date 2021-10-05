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


if __name__ == "__main__":
    unittest.main()
