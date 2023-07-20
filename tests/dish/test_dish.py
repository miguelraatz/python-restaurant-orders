from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish_1 = Dish("lasanha presunto", 25.90)
    dish_2 = Dish("lasanha berinjela", 27.00)
    dish_3 = Dish("lasanha berinjela", 27.00)

    # instance
    assert dish_1.name == "lasanha presunto"
    assert dish_1.price == 25.90
    assert dish_2.name == "lasanha berinjela"
    assert dish_2.price == 27.00

    # TypeError
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("lasanha berinjela", "27")

    # ValueError
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("lasanha berinjela", 0)

    # equal
    assert dish_2 == dish_3
    assert dish_1 != dish_3

    # hash
    assert hash(dish_2) == hash(dish_3)
    assert hash(dish_2) != hash(dish_1)

    # repr
    assert repr(dish_1) == "Dish('lasanha presunto', R$25.90)"
    assert repr(dish_3) == "Dish('lasanha berinjela', R$27.00)"

    # method add_ingredient_dependecy
    ingredient = Ingredient("carne")
    dish_1.add_ingredient_dependency(ingredient, 5)
    assert dish_1.recipe == {ingredient: 5}

    # method get_restrictions
    assert dish_1.get_restrictions() == set({
        Restriction.ANIMAL_MEAT: "ANIMAL_MEAT",
        Restriction.ANIMAL_DERIVED: "ANIMAL_DERIVED",
    })
    assert dish_1.get_ingredients() == set(dish_1.recipe.keys())
