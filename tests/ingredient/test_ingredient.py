from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501
import pytest


def test_ingredient():
    pass
    ingrediente = Ingredient("queijo parmesão")
    assert ingrediente.name == "queijo parmesão"
    ingredient = Ingredient("bacon")
    assert ingredient.name == "bacon"

    assert ingrediente.restrictions == {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient.restrictions == {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}

    assert repr(ingrediente) == "Ingredient('queijo parmesão')"
    assert repr(ingredient) == "Ingredient('bacon')"

    assert ingredient.__eq__(ingredient) == True
    assert ingrediente.__eq__(ingredient) == False

    assert ingrediente.__hash__() == ingrediente.__hash__()
    assert ingrediente.__hash__() != ingredient.__hash__()