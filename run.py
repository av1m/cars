if __name__ == "__main__":
    import cars as c
    import foods as f

    # a = foods.kebab.TruckKebab(foods.Formula("", []))
    # ab = foods.pizza.TruckPizza(foods.Formula("", []))
    # x = foods.TruckFood.from_food(foods.Pizza)
    # x = x([foods.Formula("Coca-Cola", [Pizza("tartarte", 20)])])
    # y = foods.Kebab.create_truck([foods.Formula("Coca-Cola", [Pizza("tartarte", 20)])])
    # y.add_order(1)
    # y.add_order(1)

    x = c.TruckFood.from_food(food=f.Pizza)
    print(x)
