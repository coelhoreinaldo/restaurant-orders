from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


def test_ingredient():
    banana = Ingredient("banana")

    assert banana.name == "banana"

    assert banana.restrictions == set()

    assert banana.__hash__() == hash("banana")

    assert banana.__eq__(Ingredient("banana"))

    assert banana.__repr__() == "Ingredient('banana')"
