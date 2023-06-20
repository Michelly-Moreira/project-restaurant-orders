from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish():
    ingrediente = Ingredient("queijo parmesão")
    dish1 = Dish("lasanha berinjela", 27.00)
    dish2 = Dish("lasanha presunto", 25.90)

    assert dish1.name == "lasanha berinjela"
    assert dish1.price == 27.00

    assert dish2.name == "lasanha presunto"
    assert dish2.price == 25.90

    assert dish1.__repr__() == "Dish('lasanha berinjela', R$27.00)"
    assert dish2.__repr__() == "Dish('lasanha presunto', R$25.90)"

    assert dish1.__eq__(dish2) is False
    assert dish2.__eq__(dish2) is True

    assert dish1.__hash__() != dish2.__hash__()
    assert dish2.__hash__() == dish2.__hash__()

    assert dish1.recipe == {}
    dish1.add_ingredient_dependency(ingrediente, 1)
    assert len(dish1.recipe) == 1
    assert dish1.recipe[ingrediente] == 1

    assert dish1.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
        }

    ingredients = dish1.get_ingredients()
    assert len(ingredients) == 1

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish(name="lasanha berinjela", price=None)

    with pytest.raises(ValueError):
        Dish(name="lasanha berinjela", price=0.00)
