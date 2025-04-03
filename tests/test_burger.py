import pytest

from practicum.bun import Bun
from practicum.burger import Burger
from practicum.ingredient import Ingredient


class TestBurger:
    def test_initial_burger_empty_bun_and_ingredients(self):
        # Act
        burger = Burger()
        # Assert
        assert burger.bun is None, 'Bun not empty'
        assert len(burger.ingredients) == 0 and isinstance(burger.ingredients, list), 'Invalid ingredients'

    def test_set_bun_successfully_set(self):
        # Arrange
        burger = Burger()
        bun = Bun('black bun', 100.0)
        # Act
        burger.set_buns(bun)
        # Assert
        assert burger.bun == bun, 'Mismatches in bun'

    def test_add_ingredient_succesfully_added(self):
        # Arrange
        burger = Burger()
        ingredient = Ingredient('FILLING', 'cutlet', 100.0)
        # Act
        burger.add_ingredient(ingredient)
        # Assert
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ingredient, 'Mismatches in ingredients'

    def test_remove_ingredient_succesfully_removed(self):
        # Arrange
        burger = Burger()
        ingredient = Ingredient('SAUCE', 'hot sauce', 100.0)
        burger.add_ingredient(ingredient)
        # Act
        burger.remove_ingredient(0)
        # Assert
        assert len(burger.ingredients) == 0, 'Ingredients not empty'

    def test_move_ingredient_succesfully_moved(self):
        # Arrange
        burger = Burger()
        ingredient_one = Ingredient('SAUCE', 'hot sauce', 100.0)
        ingredient_two = Ingredient('FILLING', "cutlet", 100.0)
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        # Act
        burger.move_ingredient(1, 0)
        # Assert
        assert burger.ingredients[0] == ingredient_two, 'The ingredient index has not been changed'

    def test_get_price_successfully_getted(self):
        # Arrange
        burger = Burger()
        bun = Bun("black bun", 10.0)
        ingredient_one = Ingredient('SAUCE', 'hot sauce', 40.0)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_one)
        expected_price = 60.0
        # Act
        actual_price = burger.get_price()
        # Assert
        assert pytest.approx(actual_price, abs=0.001) == pytest.approx(expected_price, abs=0.001), \
            'Mismatches in price burger'

    def test_get_receipt_successfully_getted(self):
        # Arrange
        bun = Bun("black bun", 10.0)
        ingredient_one = Ingredient('SAUCE', 'sour cream', 50.0)
        ingredient_two = Ingredient('FILLING', "cutlet", 100.0)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        expected_receipt = (f'(==== {bun.get_name()} ====)'
                            f'\n= {ingredient_one.get_type().lower()} {ingredient_one.get_name()} ='
                            f'\n= {ingredient_two.get_type().lower()} {ingredient_two.get_name()} ='
                            f'\n(==== {bun.get_name()} ====)'
                            f'\n\nPrice: {burger.get_price()}')
        # Act
        actual_receipt = burger.get_receipt()
        # Assert
        assert expected_receipt == actual_receipt, 'Mismatches in receipt'
