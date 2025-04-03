import pytest

from practicum.ingredient import Ingredient


@pytest.mark.ingredients
class TestIngredient:
    def test_create_ingredient_successfully_operation(self):
        # Arrange
        expected_ingredient_type = 'SAUCE'
        expected_name = 'Hot sauce'
        expected_price = 25.0
        # Act
        ingredient = Ingredient(expected_ingredient_type, expected_name, expected_price)
        # Assert
        assert ingredient.get_type() == expected_ingredient_type, 'The ingredient type does not match the expected one'
        assert ingredient.get_name() == expected_name, 'The ingredient name does not match the expected one'
        assert ingredient.get_price() == pytest.approx(expected_price, abs=0.001), ('The ingredient price does not '
                                                                                    'match the expected one')
