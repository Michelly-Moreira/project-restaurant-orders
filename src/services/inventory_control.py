from csv import DictReader
from typing import Dict

from models.dish import Recipe
from models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"


Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        i = 0
        for row in self.inventory:
            if row == list(recipe.keys())[i]:
                if self.inventory[row] >= int(list(recipe.values())[i]):
                    if i == len(recipe)-1:
                        return True
        return False

    def consume_recipe(self, recipe: Recipe) -> None:
        self.recipe = recipe


stock = InventoryMapping(BASE_INVENTORY)
stock.check_recipe_availability({Ingredient('queijo mussarela'): 300})
# stock.consume_recipe("cravo", 200)
