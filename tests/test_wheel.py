from unittest import TestCase

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

    def test_raise(self):
        self.assertRaises(AssertionError, lambda: Wheel(size=0))
        self.assertRaises(AssertionError, lambda: Wheel(size=-1))
        self.assertRaises(AssertionError, lambda: Wheel(size=[]))  # type: ignore
        self.assertRaises(AssertionError, lambda: Wheel(size=None))  # type: ignore
        self.assertRaises(AssertionError, lambda: Wheel(has_rim=None))  # type: ignore
        self.assertRaises(AssertionError, lambda: Wheel(has_rim=-1))  # type: ignore
        self.assertRaises(AssertionError, lambda: Wheel(has_rim=0))  # type: ignore
