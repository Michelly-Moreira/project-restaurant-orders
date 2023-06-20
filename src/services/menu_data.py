from models.dish import Dish
from models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dish = set()
        self.ingredient = set()

    def reading_file(source_path):
        with open(source_path,  encoding = "utf-8") as file:
            source = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = source
            print(header)
            print(data)
# Quando um * está presente no desempacotamento, os valores são desempacotados em formato de lista.

MenuData.reading_file("/home/michelly/Trybe/trybe-project/cs/sd-026-b-restaurant-orders/data/menu_base_data.csv")