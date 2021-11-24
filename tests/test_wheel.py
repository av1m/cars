from unittest import TestCase

from cars.car import Car
from cars.wheel import Wheel


class TestWheel(TestCase):
    def test_default(self):
        wheel: Wheel = Wheel()
        self.assertEqual(wheel.has_rim, False)
        self.assertEqual(wheel.size, 1)

    def test_simple(self):
        wheel: Wheel = Wheel(size=5, has_rim=True)
        self.assertEqual(wheel.size, 5)
        self.assertTrue(wheel.has_rim)

    def test_mutation(self):
        wheel: Wheel = Wheel(size=8, has_rim=True)
        wheel.has_rim = False
        self.assertFalse(wheel.has_rim)
        self.assertEqual(wheel.size, 8)
        wheel.size = 10
        self.assertEqual(wheel.size, 10)
        self.assertFalse(wheel.has_rim)

    def test_equals(self) -> None:
        wheel1: Wheel = Wheel(size=8, has_rim=True)
        wheel2: Wheel = Wheel(size=10, has_rim=True)
        wheel3: Wheel = Wheel(size=8, has_rim=False)
        self.assertEqual(Wheel(), Wheel())
        self.assertEqual(wheel1, Wheel(size=8, has_rim=True))
        self.assertNotEqual(wheel1, wheel2)
        self.assertNotEqual(wheel1, wheel3)
        self.assertNotEqual(wheel2, wheel3)
        self.assertNotEqual(wheel2, "this_string_isnot_a_wheel")

    def test_repr(self):
        self.assertEqual(repr(Wheel()), "Wheel(size=1, has_rim=False)")
        self.assertEqual(repr(Wheel(size=20)), "Wheel(size=20, has_rim=False)")
        self.assertEqual(repr(Wheel(size=1000)), "Wheel(size=1000, has_rim=False)")
        self.assertEqual(
            repr(Wheel(size=1000, has_rim=True)), "Wheel(size=1000, has_rim=True)"
        )
        self.assertEqual(repr(Wheel(15, True)), "Wheel(size=15, has_rim=True)")

    def test_str(self):
        self.assertEqual(str(Wheel()), "Wheel of 1 without rim")
        self.assertEqual(str(Wheel(size=20)), "Wheel of 20 without rim")
        self.assertEqual(str(Wheel(size=1000)), "Wheel of 1000 without rim")
        self.assertEqual(str(Wheel(size=1000, has_rim=True)), "Wheel of 1000 with rim")
        self.assertEqual(str(Wheel(15, True)), "Wheel of 15 with rim")

    def test_raise(self):
        self.assertRaises(AssertionError, lambda: Wheel(size=0))
        self.assertRaises(AssertionError, lambda: Wheel(size=-1))
        self.assertRaises(AssertionError, lambda: Wheel(size=[]))  # type: ignore
        self.assertRaises(AssertionError, lambda: Wheel(size=None))  # type: ignore
        self.assertRaises(AssertionError, lambda: Wheel(has_rim=None))  # type: ignore
        self.assertRaises(AssertionError, lambda: Wheel(has_rim=-1))  # type: ignore
        self.assertRaises(AssertionError, lambda: Wheel(has_rim=0))  # type: ignore

    def test_car(self):
        # Wheel --> Car
        wheel1: Wheel = Wheel(size=20, has_rim=True)
        car1: Car = Car(100, 200)
        self.assertIsNone(wheel1.car)
        self.assertEqual(car1.wheels, tuple())
        wheel1.car = car1
        self.assertEqual(wheel1.car, car1)
        self.assertEqual(car1.wheels[0], wheel1)
        self.assertEqual(len(car1.wheels), 1)
        # Car --> Wheel
        wheel2: Wheel = Wheel(size=50, has_rim=True)
        car2: Car = Car(300, 5500)
        car2.add_wheel(wheel2)
        self.assertEqual(wheel2.car, car2)
        self.assertEqual(car2.wheels[0], wheel2)
        self.assertEqual(len(car2.wheels), 1)

    def test_same(self):
        wheel1: Wheel = Wheel(size=50, has_rim=True)
        car: Car = Car()
        car2: Car = Car(max_speed=100)
        car.add_wheel(wheel1)
        car2.add_wheel(wheel1)
        self.assertEqual(wheel1.car, car)
        self.assertEqual(
            len(car2.wheels),
            0,
            msg="wheel1 is already added to car and can't associate to car2",
        )
