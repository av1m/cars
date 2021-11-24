# -*- coding: utf-8 -*-

import unittest

from foods.formula import Formula
from foods.pizza import Pizza, TruckPizza


class TestMemento(unittest.TestCase):
    foods = [
        Pizza("Margherita", 10),
        Pizza("Funghi", 12),
        Pizza("Quattro Stagioni", 14),
    ]
    formulas = [
        Formula("Coca-Cola", foods),
        Formula("Fanta", foods),
        Formula("Sprite", foods),
    ]

    def test_simple(self) -> None:
        pizza = TruckPizza(formulas=TestMemento.formulas)
        pizza.set_state()
        self.assertEqual(pizza.formulas, pizza.memento.state.get("formulas"))
        self.assertEqual(pizza.orders, ())
        self.assertEqual(pizza.memento.state.get("orders"), [])
        self.assertEqual(len(pizza.orders), 0)
        pizza.add_order(1)
        self.assertEqual(pizza.formulas, pizza.memento.state.get("formulas"))
        self.assertNotEqual(pizza.orders, pizza.memento.state.get("orders"))
        self.assertEqual(len(pizza.orders), 1)
        pizza.add_order(2)
        self.assertEqual(len(pizza.orders), 2)
        # Save the state
        pizza.set_state()
        self.assertEqual(len(pizza.orders), 2)
        pizza.add_order(2)
        self.assertEqual(len(pizza.orders), 3)
        # Restore state
        pizza.reset_state()
        self.assertEqual(len(pizza.orders), 2)
        pizza.reset_state()
        self.assertEqual(len(pizza.orders), 2)
