from models.dish import Dish
from models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()

#lendo o arquivo csv:
        with open(self.source_path, encoding="utf-8") as file:
            source = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = source
            #print(header,data)

# Quando um * está presente no desempacotamento,
# os valores são desempacotados em formato de lista.

# criando a receita:
            name = ""
            price = 0
            ingredient = ""
            amount = 0

        for i in data:
            ingredient = i[2]
            amount = int(i[3])
            if i[0] != name:
                name = i[0]
                price = float(i[1])
                #print(name, price)
                #print(ingredient, amount)
                new_dish = Dish(name, price)
                new_dish.add_ingredient_dependency(
                    Ingredient(ingredient), amount
                )
                self.dishes.add(new_dish)
            else:
                dish = list(self.dishes)[0]
                if dish.name != i[0]:
                    dish = list(self.dishes)[1]
                dish.add_ingredient_dependency(
                    Ingredient(ingredient), amount
                )

MenuData("/home/michelly/Trybe/trybe-project/cs/sd-026-b-restaurant-orders/data/menu_base_data.csv")
