# -*- coding: utf-8 -*-
import copy
import unittest

from foods.formula import Formula
from foods.kebab import Kebab
from foods.pizza import Pizza


class TestFormula(unittest.TestCase):
    def setUp(self) -> None:
        self.foods = [
            Pizza("Margarita", 10),
            Pizza("Vegetarian", 15),
            Pizza("Hawaiian", 20),
            Kebab("Chicken", 5),
            Kebab("Beef", 10),
        ]
        self.formulas = [
            Formula("Coca-Cola", [self.foods[0], self.foods[1], self.foods[2]]),
            Formula("Orangina", [self.foods[0], self.foods[1]]),
            Formula("Orangina", [self.foods[1], self.foods[2]]),
            Formula("Pepsi", [self.foods[4], self.foods[3]]),
            Formula("Water", [self.foods[4]]),
        ]

    def test_init(self) -> None:
        self.assertEqual(Formula("").foods, set())
        self.assertEqual(self.formulas[-1].foods, {self.foods[4]})

    def test_str(self) -> None:
        self.assertEqual(
            str(self.formulas[-1]),
            "For 10$, you can drink Water and eats : {Kebab(sauce='Beef', price=10)}",
        )

    def test_equals(self) -> None:
        self.assertEqual(self.formulas[0], self.formulas[0])
        self.assertNotEqual(self.formulas[0], self.formulas[1])
        self.assertNotEqual(self.formulas[1], self.formulas[2])
        self.assertNotEqual(self.formulas[0], "Hello World")
        self.assertEqual(
            self.formulas[0],
            Formula("Coca-Cola", [self.foods[0], self.foods[1], self.foods[2]]),
        )

    def test_add_food(self) -> None:
        formula = Formula("Coca-Cola", [self.foods[0], self.foods[1], self.foods[2]])
        self.assertEqual(len(formula.foods), 3)
        formula.add_food(self.foods[3])
        self.assertEqual(len(formula.foods), 4)
        # Check set (no duplicate food)
        formula.add_food(self.foods[3])
        self.assertEqual(len(formula.foods), 4)
