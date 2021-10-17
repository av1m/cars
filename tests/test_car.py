# -*- coding: utf-8 -*-

import unittest

from cars.car import Car
from cars.motor import Motor, TypeMotor
from cars.wheel import Wheel


class TestCar(unittest.TestCase):
    def test_default(self) -> None:
        car = Car()
        self.assertEqual(car.horse_power, 0)
        self.assertEqual(car.max_speed, 0)
        self.assertEqual(car.motor, Motor(0))
        self.assertEqual(car.wheels, tuple())

    def test_simple(self) -> None:
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

    def test_raise(self) -> None:
        self.assertRaises(AssertionError, lambda: Car(max_speed=-1))
        self.assertRaises(AssertionError, lambda: Car(horse_power=-1))
        self.assertRaises(AssertionError, lambda: Car(wheels=Wheel()))  # type: ignore

    def test_getters(self) -> None:
        car = Car(max_speed=100, horse_power=150)
        self.assertEqual(car.horse_power, 150)
        self.assertEqual(car.max_speed, 100)

    def test_setters(self) -> None:
        car = Car(max_speed=100, horse_power=150)
        car.horse_power = 200
        self.assertEqual(car.horse_power, 200)
        self.assertEqual(car.max_speed, 100)
        car.max_speed = 120
        self.assertEqual(car.max_speed, 120)
        self.assertEqual(car.horse_power, 200)
        with self.assertRaises(AssertionError):
            car.max_speed = -1
            car.horse_power = -10
            car.max_speed = None  # type: ignore
            car.horse_power = None  # type: ignore
        self.assertEqual(car.max_speed, 120)
        self.assertEqual(car.horse_power, 200)
        self.assertEqual(car.motor.type_motor, TypeMotor.RACING)
        self.assertEqual(car.wheels, ())

    def test_init(self) -> None:
        car = Car()
        self.assertEqual(car.horse_power, 0)
        self.assertEqual(car.max_speed, 0)
        self.assertEqual(car.wheels, tuple())
        self.assertEqual(car.motor, Motor(0))
        car = Car(max_speed=100, horse_power=150)
        self.assertEqual(car.horse_power, 150)
        self.assertEqual(car.max_speed, 100)
        self.assertEqual(car.wheels, tuple())
        self.assertEqual(car.motor, Motor(150))
        car = Car(
            max_speed=10, horse_power=20, wheels=[Wheel(size=5, has_rim=False)] * 4
        )
        self.assertEqual(car.horse_power, 20)
        self.assertEqual(car.max_speed, 10)
        self.assertEqual(car.wheels, tuple([Wheel(size=5, has_rim=False)] * 4))
        self.assertEqual(car.motor, Motor(20))

    def test_equals(self) -> None:
        car1: Car = Car(max_speed=100, horse_power=150)
        car2: Car = Car(max_speed=100, horse_power=150)
        car3: Car = Car(max_speed=100, horse_power=200)
        car4: Car = Car(max_speed=200, horse_power=150)
        self.assertEqual(car1, car2)
        self.assertNotEqual(car1, car3)
        self.assertNotEqual(car1, car4)
        self.assertNotEqual(car2, car3)
        self.assertNotEqual(car2, car4)
        self.assertNotEqual(car3, car4)
        car = Car(
            max_speed=10, horse_power=20, wheels=[Wheel(size=5, has_rim=False)] * 6
        )
        self.assertEqual(
            car,
            Car(
                max_speed=10, horse_power=20, wheels=[Wheel(size=5, has_rim=False)] * 6
            ),
        )

    def test_improve(self) -> None:
        car: Car = Car(max_speed=40, horse_power=400)
        car.improve(new_max_speed=1000, new_horse_power=500)
        self.assertEqual(car.horse_power, 500)
        self.assertEqual(car.max_speed, 1000)
        self.assertRaises(AssertionError, lambda: car.improve(-1, 500))
        self.assertRaises(AssertionError, lambda: car.improve(500, -1))

    def test_motor(self) -> None:
        car = Car(horse_power=150)
        self.assertEqual(car.horse_power, 150)
        self.assertEqual(car.motor, Motor(150))
        self.assertEqual(car.motor.type_motor, TypeMotor.SPORT)
        car.horse_power = 500
        self.assertEqual(car.horse_power, 500)
        self.assertEqual(car.motor, Motor(500))

    def test_wheels(self) -> None:
        car = Car()
        self.assertEqual(car.wheels, tuple())
        car = Car(wheels=[Wheel(size=5, has_rim=False)] * 4)
        self.assertEqual(len(car._wheels), 4)
        self.assertEqual(len(car.wheels), 4)
        car.add_wheel(Wheel(size=50, has_rim=True))
        self.assertEqual(len(car.wheels), 5)
        self.assertTrue(Wheel(size=50, has_rim=True) in car.wheels)


if __name__ == "__main__":
    unittest.main()
