from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():

    ingrediente = Ingredient("queijo parmesão")
    assert ingrediente.name == "queijo parmesão"
    ingredient = Ingredient("bacon")
    assert ingredient.name == "bacon"

    assert ingrediente.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
        }
    assert ingredient.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED
        }

    assert ingrediente.__repr__(ingrediente) == "Ingredient('queijo parmesão')"
    assert ingrediente.__repr__(ingredient) == "Ingredient('bacon')"

    assert ingredient.__eq__(ingredient) is True
    assert ingrediente.__eq__(ingredient) is False

    assert ingrediente.__hash__() == ingrediente.__hash__()
    assert ingrediente.__hash__() != ingredient.__hash__()
