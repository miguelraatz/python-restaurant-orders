# Req 3
from models.dish import Dish
from models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self._data = []
        self.dishes: Dish = set()
        list = dict()

        with open(source_path, "r") as file:
            reader = csv.reader(file)
            header, *rows = reader
            self._data = rows

        for dish, price, ingredient, recipe_amount in self._data:
            if dish not in list:
                dishes_add = Dish(dish, float(price))
                list[dish] = dishes_add

            ingredient_add = Ingredient(ingredient)

            list[dish].add_ingredient_dependency(
                ingredient_add, int(recipe_amount)
            )

        self.dishes.update(list.values())
