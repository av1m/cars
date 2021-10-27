# -*- coding: utf-8 -*-

import unittest

from cars.motor import Motor, TypeMotor


class TestMotor(unittest.TestCase):
    def test_empty(self) -> None:
        motor: Motor = Motor(horsepower=0)
        self.assertEqual(motor.type_motor, TypeMotor.EMPTY)

    def test_compute(self) -> None:
        self.assertEqual(Motor.compute_type(horsepower=0), TypeMotor.EMPTY)
        self.assertEqual(Motor.compute_type(horsepower=50), TypeMotor.CITY)
        self.assertEqual(Motor.compute_type(horsepower=150), TypeMotor.SPORT)
        self.assertEqual(Motor.compute_type(horsepower=250), TypeMotor.RACING)
        self.assertEqual(Motor.compute_type(horsepower=350), TypeMotor.F1)

    def test_raise(self) -> None:
        self.assertRaises(AssertionError, lambda: Motor(horsepower=-1))
        self.assertRaises(AssertionError, lambda: Motor(horsepower=None))  # type: ignore
        self.assertRaises(AssertionError, lambda: Motor(horsepower="1"))  # type: ignore
        self.assertRaises(AssertionError, lambda: Motor.compute_type(horsepower=-1))  # type: ignore
        self.assertRaises(TypeError, lambda: Motor.compute_type(horsepower=None))  # type: ignore

    def test_interval(self) -> None:
        self.assertEqual(Motor(horsepower=50).type_motor, TypeMotor.CITY)
        self.assertEqual(Motor(horsepower=150).type_motor, TypeMotor.SPORT)
        self.assertEqual(Motor(horsepower=250).type_motor, TypeMotor.RACING)
        self.assertEqual(Motor(horsepower=350).type_motor, TypeMotor.F1)

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
            motor: Motor = Motor(horsepower=type_motor[1])
            self.assertEqual(motor.type_motor, type_motor[0])

    def test_equals(self) -> None:
        motor: Motor = Motor(horsepower=0)
        self.assertEqual(motor, Motor(0))
        motor = Motor(horsepower=150)
        self.assertEqual(motor, Motor(150))
        self.assertNotEqual(motor, Motor(900))

    def test_lt(self) -> None:
        types: list[TypeMotor] = list(TypeMotor)
        last: TypeMotor = types.pop(0)
        t: TypeMotor
        for t in types:
            self.assertLess(last, t)
            last = t

    def test_iter(self) -> None:
        types: list[TypeMotor] = list(TypeMotor)
        for i, t in enumerate(types):
            self.assertEqual(types[i], t)

    def test_next(self) -> None:
        self.assertEqual(next(TypeMotor.EMPTY), TypeMotor.CITY)
        self.assertEqual(next(TypeMotor.CITY), TypeMotor.SPORT)
        self.assertEqual(next(TypeMotor.SPORT), TypeMotor.RACING)
        self.assertEqual(next(TypeMotor.RACING), TypeMotor.F1)
        self.assertEqual(next(TypeMotor.F1), TypeMotor.F1)

    def test_minmax(self) -> None:
        self.assertEqual(min(TypeMotor), TypeMotor.EMPTY)
        self.assertEqual(max(TypeMotor), TypeMotor.F1)


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

    def test_hash(self) -> None:
        self.assertEqual(hash(Motor(0)), hash(Motor(0)))
        self.assertEqual(hash(Motor(100)), hash(Motor(100)))
        self.assertEqual(hash(Motor(100)), hash(Motor(101)))
        self.assertNotEqual(hash(Motor(100)), hash(Motor(200)))

    def test_lt(self) -> None:
        motor: Motor = Motor(horsepower=0)
        self.assertLess(motor, Motor(50))
        self.assertLess(motor, Motor(150))
        self.assertGreater(Motor(250), motor)
        self.assertEquals(motor, Motor(0))


if __name__ == "__main__":
    unittest.main()
