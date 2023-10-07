import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self.load_data()

    def load_data(self):
        with open(self.source_path, "r") as file:
            lines = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = lines

            dishes_collection = set()

            for dish_name, price, ingredient, amount in data:
                curr_dish = Dish(dish_name, float(price))
                dishes_collection.add(curr_dish)
                for dish in list(dishes_collection):
                    if dish.name == dish_name:
                        dish.add_ingredient_dependency(
                            Ingredient(ingredient),
                            int(amount),
                        )

            return dishes_collection
