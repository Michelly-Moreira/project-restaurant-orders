from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


def test_dish():
    pass
    dish1 = Dish("lasanha berinjela", 27.00)
    dish2 = Dish("lasanha presunto", 25.90)

    assert dish1.name == "lasanha berinjela"
    assert dish1.price == 27.00
    assert dish1.recipe == {}

    assert dish2.name == "lasanha presunto"
    assert dish2.price == 25.90
