import pytest

from practicum.ingredient import Ingredient


@pytest.mark.ingredients
class TestIngredient:
    def test_create_ingredient_successfully_operation(self):
        # Arrange
        ingredient_type = 'SAUCE'
        name = 'Hot sauce'
        price = 25.0
        # Act
        ingredient = Ingredient(ingredient_type, name, price)
        # Assert
        assert ingredient.get_type() == ingredient_type, 'The ingredient type does not match the expected one'
        assert ingredient.get_name() == name, 'The ingredient name does not match the expected one'
        assert ingredient.get_price() == pytest.approx(price, abs=0.001), ('The ingredient price does not match '
                                                                           'the expected one')
