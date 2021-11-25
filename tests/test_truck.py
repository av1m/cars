# -*- coding: utf-8 -*-

import unittest

from cars.truck import TruckFood
from foods.food import Food
from foods.formula import Formula
from foods.kebab import Kebab, TruckKebab
from foods.pizza import Pizza, TruckPizza


class TestTruck(unittest.TestCase):
    def setUp(self) -> None:
        self.foods = [
            Pizza("Margarita", 10),
            Pizza("Vegetarian", 15),
            Pizza("Hawaiian", 20),
            Kebab("Chicken", 5),
            Kebab("Beef", 10),
        ]
        self.formulas = {
            Formula("Coca-Cola", [self.foods[0], self.foods[1], self.foods[2]]),
            Formula("Orangina", [self.foods[0], self.foods[1]]),
            Formula("Pepsi", [self.foods[4], self.foods[3]]),
            Formula("Water", [self.foods[4]]),
        }

    def test_meta(self) -> None:
        self.assertEqual(TruckFood.__name__, "TruckFood")
        self.assertEqual(TruckKebab.__name__, "TruckKebab")
        self.assertEqual(TruckPizza.__name__, "TruckPizza")
        self.assertRaises(TypeError, lambda: Food.get_truck())
        self.assertRaises(TypeError, lambda: Food.create_truck())
        # https://stackoverflow.com/a/44259123
        self.assertRaises(TypeError, lambda: TruckFood())  # type: ignore
        self.assertIs(TruckFood, TruckFood(self.formulas).__class__)

    def test___init_subclass__(self) -> None:
        self.assertRaises(AttributeError, lambda: type("TruckF", (TruckFood,), {}))
        self.assertRaises(
            AttributeError, lambda: type("T", (TruckFood,), {"food": "Pizza"})
        )
        self.assertRaises(
            AttributeError, lambda: type("T", (TruckFood,), {"food": type("_", (), {})})
        )

    def test_init(self) -> None:
        truck_pizza = TruckPizza(self.formulas)
        self.assertIsInstance(truck_pizza, TruckPizza)
        self.assertEqual(truck_pizza.food, Pizza)
        self.assertEqual(truck_pizza.orders, ())
        self.assertEqual(list(truck_pizza.formulas.values()), list(self.formulas))

    def test_orders(self) -> None:
        truck_kebab = TruckKebab(self.formulas)
        self.assertEqual(truck_kebab.orders, ())
        for i in range(1, 5):
            truck_kebab.add_order(i)
            # (1,), (1,2,), (1,2,3,), (1,2,3,4,), ....
            expected = tuple(range(1, i + 1))
            self.assertEqual(truck_kebab.orders, expected)
        self.assertRaises(ValueError, lambda: truck_kebab.add_order(0))
        self.assertRaises(ValueError, lambda: truck_kebab.add_order(10))

    def test_get_truck(self) -> None:
        self.assertEqual(Pizza.get_truck(), TruckPizza)
        self.assertEqual(Kebab.get_truck(), TruckKebab)
        # Create object manually
        truck_type = Pizza.get_truck()
        self.assertNotIsInstance(truck_type, TruckPizza)
        truck = truck_type(formulas=self.formulas)
        self.assertIsInstance(truck, TruckPizza)

    def test_create_truck(self) -> None:
        self.assertRaises(TypeError, lambda: Pizza.create_truck())
        self.assertRaises(TypeError, lambda: Kebab.create_truck())
        truck = Pizza.create_truck(formulas=self.formulas)
        self.assertIsInstance(truck, TruckPizza)
        self.assertListEqual(list(truck.formulas.values()), list(self.formulas))

    def test_undo(self) -> None:
        truck_kebab = TruckKebab(self.formulas)
        self.assertRaises(IndexError, lambda: truck_kebab.undo_last_order())
        truck_kebab.add_order(1)
        truck_kebab.add_order(2)
        self.assertEqual(truck_kebab.orders, (1, 2))
        last_order = truck_kebab.undo_last_order()
        self.assertEqual(truck_kebab.orders, (1,))
        self.assertEqual(last_order, (2, truck_kebab.formulas.get(2)))

    def test_str(self) -> None:
        self.assertEqual(
            str(TruckPizza(self.formulas)),
            "This TruckPizza at a maximum speed of 0 km/h using its Motor EMPTY, "
            "its 0 hp and its 0 wheels and can sell Pizza",
        )
        self.assertEqual(
            str(TruckKebab(self.formulas)),
            "This TruckKebab at a maximum speed of 0 km/h using its Motor EMPTY, "
            "its 0 hp and its 0 wheels and can sell Kebab",
        )

    def test_repr(self) -> None:
        self.assertEqual(
            repr(TruckPizza([Formula("Coca-Cola", [Pizza("Margarita", 10)])])),
            """TruckPizza({1: Formula('Coca-Cola', {Pizza(sauce='Margarita', price=10)})})""",
        )
