from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
import pytest


def test_ingredient():
    pass
    ingrediente = Ingredient("queijo parmesão")
    assert ingrediente.name == "queijo parmesão"

    ingredient = Ingredient("bacon")
    assert ingredient.name == "bacon"

