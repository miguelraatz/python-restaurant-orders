from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    # Instance
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    ingredient3 = Ingredient("ovo")
    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)

    # repr
    assert repr(ingredient1) == "Ingredient('queijo mussarela')"
    assert ingredient3.name == "ovo"

    # equal
    assert ingredient1 == ingredient2
    assert ingredient2 != ingredient3

    # restrictions
    assert ingredient1.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    assert ingredient3.restrictions == {Restriction.ANIMAL_DERIVED}
