from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


def test_dish():
    pass
    dish = Dish("lasanha berinjela", 27.00)
    
    assert dish.name == "lasanha berinjela"
    assert dish.price == 27.00
    assert dish.recipe == {}
