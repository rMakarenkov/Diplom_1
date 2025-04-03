import pytest

from practicum.bun import Bun
from practicum.database import Database
from practicum.ingredient import Ingredient


@pytest.mark.databases
class TestDatabase:
    def test_initial_database_bun_successfully_initial(self):
        # Arrange
        expected_buns_list = [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300)
        ]
        # Act
        db = Database()
        # Assert
        assert len(db.available_buns()) == len(expected_buns_list), ('Buns list length mismatches during database '
                                                                     'initialization')
        for bun_act, bun_exp in zip(expected_buns_list, db.available_buns()):
            assert bun_act.name == bun_exp.name, 'Mismatches in the name Buns'
            assert bun_act.price == bun_exp.price, 'Mismatches in the price Buns'

    def test_initial_database_ingredient_successfully_initial(self):
        # Arrange
        expected_ingredients_list = [
            Ingredient('SAUCE', "hot sauce", 100.0),
            Ingredient('SAUCE', "sour cream", 200.0),
            Ingredient('SAUCE', "chili sauce", 300.0),
            Ingredient('FILLING', "cutlet", 100.0),
            Ingredient('FILLING', "dinosaur", 200.0),
            Ingredient('FILLING', "sausage", 300.0)
        ]
        # Act
        db = Database()
        # Assert
        assert len(db.available_ingredients()) == len(expected_ingredients_list), ('Ingredients list length mismatches '
                                                                                   'during database initialization')
        for ingredient_act, ingredient_exp in zip(db.available_ingredients(), expected_ingredients_list):
            assert ingredient_act.name == ingredient_exp.name, 'Mismatches in the name Ingredients'
            assert ingredient_act.price == ingredient_exp.price, 'Mismatches in the price'
            assert ingredient_act.type == ingredient_exp.type, 'Mismatches in the type'
