# -*- coding: utf-8 -*-

import unittest

import cars as c
import foods as f


class TestTruck(unittest.TestCase):
    def setUp(self) -> None:
        self.foods = [
            f.Pizza("Margarita", 10),
            f.Pizza("Vegetarian", 15),
            f.Pizza("Hawaiian", 20),
            f.Kebab("Chicken", 5),
            f.Kebab("Beef", 10),
        ]
        self.formulas = {
            f.Formula("Coca-Cola", [self.foods[0], self.foods[1], self.foods[2]]),
            f.Formula("Orangina", [self.foods[0], self.foods[1]]),
            f.Formula("Pepsi", [self.foods[4], self.foods[3]]),
            f.Formula("Water", [self.foods[4]]),
        }

    def test_meta(self) -> None:
        self.assertEqual(c.TruckFood.__name__, "TruckFood")
        self.assertEqual(f.TruckKebab.__name__, "TruckKebab")
        self.assertEqual(f.TruckPizza.__name__, "TruckPizza")
        self.assertRaises(TypeError, lambda: f.Food.get_truck())
        self.assertRaises(TypeError, lambda: f.Food.create_truck())
        self.assertRaises(TypeError, lambda: c.TruckFood())  # type: ignore
        self.assertRaises(TypeError, lambda: c.TruckFood(self.formulas))

    def test_get_truck(self) -> None:
        self.assertEqual(f.Pizza.get_truck(), f.TruckPizza)
        self.assertEqual(f.Kebab.get_truck(), f.TruckKebab)
        # Create object manually
        truck_type = f.Pizza.get_truck()
        self.assertNotIsInstance(truck_type, f.TruckPizza)
        truck = truck_type(formulas=self.formulas)
        self.assertIsInstance(truck, f.TruckPizza)

    def test_create_truck(self) -> None:
        self.assertRaises(TypeError, lambda: f.Pizza.create_truck())
        self.assertRaises(TypeError, lambda: f.Kebab.create_truck())
        truck = f.Pizza.create_truck(formulas=self.formulas)
        self.assertIsInstance(truck, f.TruckPizza)
