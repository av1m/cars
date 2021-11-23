# -*- coding: utf-8 -*-

import copy
import unittest

from cars import Car, Motor, TypeMotor, Wheel


class TestCar(unittest.TestCase):
    def setUp(self) -> None:
        self.car0: Car = Car()
        self.car1: Car = Car(max_speed=100, horsepower=150)
        self.car2: Car = Car(max_speed=100, horsepower=150)
        self.car3: Car = Car(max_speed=150, horsepower=150)
        self.car4: Car = Car(max_speed=150, horsepower=100)

    def test_default(self) -> None:
        car = self.car0
        self.assertEqual(car.horsepower, 0)
        self.assertEqual(car.max_speed, 0)
        self.assertEqual(car.motor, Motor(0))
        self.assertEqual(car.wheels, tuple())

    def test_simple(self) -> None:
        car: Car = Car(
            max_speed=99, horsepower=100, wheels=[Wheel(size=5, has_rim=False)] * 4
        )
        self.assertEqual(car.horsepower, 100)
        self.assertEqual(car.max_speed, 99)
        self.assertEqual(car.motor, Motor(car.horsepower))
        self.assertEqual(car.motor.type_motor, TypeMotor.SPORT)
        self.assertIsInstance(car.wheels, tuple)
        self.assertEqual(len(car.wheels), 4)
        for wheel in car.wheels:
            self.assertEqual(wheel, Wheel(size=5, has_rim=False))

    def test_raise(self) -> None:
        self.assertRaises(AssertionError, lambda: Car(max_speed=-1))
        self.assertRaises(AssertionError, lambda: Car(horsepower=-1))
        self.assertRaises(AssertionError, lambda: Car(wheels=Wheel()))  # type: ignore

    def test_getters(self) -> None:
        car = Car(max_speed=100, horsepower=150)
        self.assertEqual(car.horsepower, 150)
        self.assertEqual(car.max_speed, 100)

    def test_setters(self) -> None:
        car = self.car1
        car.horsepower = 200
        self.assertEqual(car.horsepower, 200)
        self.assertEqual(car.max_speed, 100)
        car.max_speed = 120
        self.assertEqual(car.max_speed, 120)
        self.assertEqual(car.horsepower, 200)
        self.assertRaises(AssertionError, lambda: setattr(car, "max_speed", -1))
        self.assertRaises(AssertionError, lambda: setattr(car, "horsepower", -10))
        self.assertRaises(
            AssertionError, lambda: setattr(car, "max_speed", None)
        )  # type: ignore
        self.assertRaises(AssertionError, lambda: setattr(car, "horsepower", None))  # type: ignore
        self.assertEqual(car.max_speed, 120)
        self.assertEqual(car.horsepower, 200)
        self.assertEqual(car.motor.type_motor, TypeMotor.RACING)
        self.assertEqual(car.wheels, ())

    def test_init(self) -> None:
        car = self.car0
        self.assertEqual(car.horsepower, 0)
        self.assertEqual(car.max_speed, 0)
        self.assertEqual(car.wheels, tuple())
        self.assertEqual(car.motor, Motor(0))
        car = self.car1
        self.assertEqual(car.horsepower, 150)
        self.assertEqual(car.max_speed, 100)
        self.assertEqual(car.wheels, tuple())
        self.assertEqual(car.motor, Motor(150))
        car = Car(
            max_speed=10, horsepower=20, wheels=[Wheel(size=5, has_rim=False)] * 4
        )
        self.assertEqual(car.horsepower, 20)
        self.assertEqual(car.max_speed, 10)
        self.assertEqual(car.wheels, tuple([Wheel(size=5, has_rim=False)] * 4))
        self.assertEqual(car.motor, Motor(20))

    def test_str(self) -> None:
        str_car = "This Car at a maximum speed of 0 km/h using its Motor EMPTY, its 0 hp and its 0 wheels"
        self.assertEqual(str(self.car0), str_car)

    def test_repr(self) -> None:
        repr_car = "Car(max_speed=0, horsepower=0, motor=Motor EMPTY, color=#ffffff)"
        self.assertEqual(repr(self.car0), repr_car)

    def test_equals(self) -> None:
        self.assertEqual(self.car1, self.car2)
        self.assertNotEqual(self.car1, self.car3)
        self.assertNotEqual(self.car1, self.car4)
        self.assertNotEqual(self.car2, self.car3)
        self.assertNotEqual(self.car2, self.car4)
        self.assertNotEqual(self.car3, self.car4)
        car = Car(
            max_speed=10, horsepower=20, wheels=[Wheel(size=5, has_rim=False)] * 6
        )
        self.assertEqual(
            car,
            Car(max_speed=10, horsepower=20, wheels=[Wheel(size=5, has_rim=False)] * 6),
        )
        self.assertNotEqual(car, "this_string_isnot_a_car")

    def test_improve(self) -> None:
        car: Car = Car(max_speed=40, horsepower=400)
        car.improve(new_max_speed=1000, new_horsepower=500)
        self.assertEqual(car.horsepower, 500)
        self.assertEqual(car.max_speed, 1000)
        self.assertRaises(AssertionError, lambda: car.improve(-1, 500))
        self.assertRaises(AssertionError, lambda: car.improve(500, -1))

    def test_motor(self) -> None:
        car = Car(horsepower=150)
        self.assertEqual(car.horsepower, 150)
        self.assertEqual(car.motor, Motor(150))
        self.assertEqual(car.motor.type_motor, TypeMotor.SPORT)
        car.horsepower = 500
        self.assertEqual(car.horsepower, 500)
        self.assertEqual(car.motor, Motor(500))

    def test_wheels(self) -> None:
        car: Car = self.car0
        self.assertEqual(car.wheels, tuple())
        car = Car(wheels=[Wheel(size=5, has_rim=False)] * 4)
        self.assertEqual(len(car._wheels), 4)
        self.assertEqual(len(car.wheels), 4)
        car.add_wheel(Wheel(size=50, has_rim=True))
        self.assertEqual(len(car.wheels), 5)
        self.assertTrue(Wheel(size=50, has_rim=True) in car.wheels)

    def test_color(self) -> None:
        car: Car = self.car0
        self.assertIsInstance(car.color, str)
        self.assertNotEqual(car.color, "")
        self.assertRaises(AssertionError, lambda: setattr(car, "color", None))
        self.assertRaises(AssertionError, lambda: setattr(car, "color", "red"))
        self.assertRaises(AssertionError, lambda: setattr(car, "color", "#EDJIHF"))
        self.assertRaises(AssertionError, lambda: setattr(car, "color", "FFFFFF"))
        car.color = "#EEEEEE"
        self.assertEqual(car.color.lower(), "#EEEEEE".lower())

    def test_weight(self) -> None:
        self.assertEqual(self.car0.weight, 0)
        self.car0.weight = 100
        self.assertEqual(self.car0.weight, 100)
        self.assertRaises(AssertionError, lambda: setattr(self.car0, "weight", -1))
        self.assertRaises(AssertionError, lambda: setattr(self.car0, "weight", "hello"))
        self.assertRaises(AssertionError, lambda: setattr(self.car0, "weight", None))

    def test_is_conform(self) -> None:
        car: Car = Car()
        self.assertTrue(car.is_conform())
        self.assertFalse(Car(max_speed=100, horsepower=1000).is_conform())
        self.assertTrue(Car(max_speed=100, horsepower=100).is_conform())
        self.assertTrue(Car(max_speed=120, horsepower=100).is_conform())
        self.assertTrue(Car(max_speed=1, horsepower=99).is_conform())
        self.assertFalse(Car(max_speed=1000, horsepower=0).is_conform())
        self.assertTrue(Car(max_speed=1000, horsepower=300).is_conform())

    def test_ordering(self) -> None:
        self.assertEqual(self.car1, self.car2)
        self.assertGreater(self.car3, self.car2)
        self.assertGreater(self.car3, self.car1)
        self.assertLess(self.car4, self.car3)
        self.assertLess(self.car4, self.car1)
        self.assertLess(self.car4, self.car2)

    def test_hash(self) -> None:
        self.assertEqual(hash(self.car1), hash(copy.deepcopy(self.car1)))
        self.assertEqual(hash(self.car1), hash(self.car2))
        self.assertNotEqual(hash(self.car1), hash(self.car3))
        self.assertNotEqual(hash(self.car1), hash(self.car4))
        self.assertNotEqual(hash(self.car2), hash(self.car3))
        self.assertNotEqual(hash(self.car4), hash(self.car3))
