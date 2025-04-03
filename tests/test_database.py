from practicum.bun import Bun
from practicum.database import Database
from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


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
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
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
