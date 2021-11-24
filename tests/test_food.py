# -*- coding: utf-8 -*-

import unittest

from foods import Food, Kebab, Pizza


class TestFood(unittest.TestCase):
    def test_meta(self) -> None:
        self.assertRaises(TypeError, lambda: Food())  # type: ignore
        self.assertRaises(TypeError, lambda: Food().price)  # type: ignore
        self.assertEqual(Food.__name__, "Food")
        self.assertEqual(Kebab.__name__, "Kebab")
        self.assertEqual(Pizza.__name__, "Pizza")


class TestKebab(unittest.TestCase):
    def test_str(self) -> None:
        kebab = Kebab("Tartar", 10)
        self.assertEqual(str(kebab), "Kebab with sauce Tartar and price 10")

    def test_repr(self) -> None:
        kebab = Kebab("Tartar", 10)
        self.assertEqual(repr(kebab), "Kebab(sauce='Tartar', price=10)")

    def test_init(self) -> None:
        kebab = Kebab("Tartar", 10)
        self.assertEqual(kebab.sauce, "Tartar")
        self.assertEqual(kebab.price, 10)
        self.assertRaises(ValueError, lambda: Kebab("T", -10))
        self.assertRaises(ValueError, lambda: Kebab("T", -1))

    def test_eq(self) -> None:
        kebab1 = Kebab("Tartar", 10)
        kebab2 = Kebab("Tartare", 10)
        kebab3 = Kebab("Tartar", 12)
        kebab4 = Kebab("Tartar", 12)
        self.assertNotEqual(kebab1, kebab2)
        self.assertNotEqual(kebab1, kebab3)
        self.assertNotEqual(kebab2, kebab3)
        self.assertEqual(kebab4, kebab3)
        self.assertEqual(kebab1, kebab1)


class TestPizza(unittest.TestCase):
    def test_str(self) -> None:
        pizza = Pizza("Spicy", 15)
        self.assertEqual(str(pizza), "Pizza with sauce Spicy and price 15")

    def test_repr(self) -> None:
        pizza = Pizza("Spicy", 10)
        self.assertEqual(repr(pizza), "Pizza(sauce='Spicy', price=10)")

    def test_init(self) -> None:
        pizza = Pizza("Spicy", 10)
        self.assertEqual(pizza.sauce, "Spicy")
        self.assertEqual(pizza.price, 10)
        self.assertRaises(ValueError, lambda: Pizza("T", -10))
        self.assertRaises(ValueError, lambda: Pizza("T", -1))

    def test_eq(self) -> None:
        pizza1 = Kebab("Spicy", 10)
        pizza2 = Kebab("Spicies", 10)
        pizza3 = Kebab("Spicy", 12)
        pizza4 = Kebab("Spicy", 12)
        self.assertNotEqual(pizza1, pizza2)
        self.assertNotEqual(pizza1, pizza3)
        self.assertNotEqual(pizza2, pizza3)
        self.assertEqual(pizza4, pizza3)
        self.assertEqual(pizza1, pizza1)
