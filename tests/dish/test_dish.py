from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction

# import pytest


def test_dish():
    strogonoff_de_frango = Dish("strogonoff_de_frango", 17.50)

    assert strogonoff_de_frango.name == "strogonoff_de_frango"
    assert strogonoff_de_frango.price == 17.50
    assert strogonoff_de_frango.recipe == {}

    assert (
        strogonoff_de_frango.__repr__()
        == "Dish('strogonoff_de_frango', R$17.50)"
    )

    assert strogonoff_de_frango.__eq__(Dish("strogonoff_de_frango", 17.50))

    assert strogonoff_de_frango.__hash__() == hash(
        "Dish('strogonoff_de_frango', R$17.50)"
    )

    frango = Ingredient("frango")
    creme_de_leite = Ingredient("creme de leite")

    strogonoff_de_frango.add_ingredient_dependency(frango, 2)
    strogonoff_de_frango.add_ingredient_dependency(creme_de_leite, 1)

    assert strogonoff_de_frango.recipe == {
        Ingredient("frango"): 2,
        Ingredient("creme de leite"): 1,
    }

    assert strogonoff_de_frango.get_ingredients() == {
        Ingredient("frango"),
        Ingredient("creme de leite"),
    }

    assert strogonoff_de_frango.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }
