import pytest

from practicum.bun import Bun
from practicum.database import Database
from practicum.ingredient import Ingredient


@pytest.mark.databases
class TestDatabase:

    @pytest.mark.parametrize("expected_bun", [
        Bun("black bun", 100),
        Bun("white bun", 200),
        Bun("red bun", 300)
    ])
    def test_initial_database_bun_successfully_initial(self, expected_bun):
        # Act
        db = Database()
        actual_buns = db.available_buns()
        # Assert
        assert any(bun.name == expected_bun.name and bun.price == expected_bun.price for bun in actual_buns), \
            f"Bun {expected_bun.name} with price {expected_bun.price} not found in database"

    @pytest.mark.parametrize("expected_ingredient", [
        Ingredient('SAUCE', "hot sauce", 100.0),
        Ingredient('SAUCE', "sour cream", 200.0),
        Ingredient('SAUCE', "chili sauce", 300.0),
        Ingredient('FILLING', "cutlet", 100.0),
        Ingredient('FILLING', "dinosaur", 200.0),
        Ingredient('FILLING', "sausage", 300.0)
    ])
    def test_initial_database_ingredient_successfully_initial(self, expected_ingredient):
        # Act
        db = Database()
        actual_ingredients = db.available_ingredients()
        # Assert
        assert any(ing.name == expected_ingredient.name and ing.price == expected_ingredient.price and
                   ing.type == expected_ingredient.type for ing in actual_ingredients), \
            f'Ingredient {expected_ingredient.name} with price {expected_ingredient.price} and type {expected_ingredient.type} not found in database'
