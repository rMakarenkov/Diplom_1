import pytest

from practicum import ingredient_types as ie
from practicum.ingredient import Ingredient


class TestIngredient:
    def test_create_ingredient_successfully_operation(self):
        # Arrange
        expected_ingredient_type = ie.INGREDIENT_TYPE_SAUCE
        expected_name = 'Hot sauce'
        expected_price = 25.0
        # Act
        ingredient = Ingredient(ingredient_type=expected_ingredient_type, name=expected_name, price=expected_price)
        # Assert
        assert ingredient.get_type() == expected_ingredient_type, 'The ingredient type does not match the expected one'
        assert ingredient.get_name() == expected_name, 'The ingredient name does not match the expected one'
        assert ingredient.get_price() == pytest.approx(expected_price), ('The ingredient price does not match the '
                                                                         'expected one')
