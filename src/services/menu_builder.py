from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
from models.ingredient import Restriction, Ingredient

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def get_main_menu(self, restriction=None) -> List[Dict]:
        self.restriction = restriction
        inventory = self.inventory
        dishes = []

        for dish in self.menu_data.dishes:
            print(self.menu_data.dishes)
            inventory_base = inventory.check_recipe_availability(dish.recipe)
            if inventory_base is True:
                if self.restriction not in dish.get_restrictions():
                    dishes_not_restrictions = {
                        "dish_name": dish.name,
                        "ingredients": list(dish.get_ingredients()),
                        "price": dish.price,
                        "restrictions": list(dish.get_restrictions()),
                    }
                    dishes.append(dishes_not_restrictions)
        # print(dishes)
        return dishes

    # retorna os pratos que não tem tal restrição
    # return List[Dict]


MenuBuilder().get_main_menu(Restriction.ANIMAL_DERIVED)
stock = InventoryMapping(INVENTORY_PATH)
stock.check_recipe_availability({Ingredient('cane'): 20})
