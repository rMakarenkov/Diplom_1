import pytest

from practicum.bun import Bun


class TestBun:
    def test_create_bun_successfully_operation(self):
        # Arrange
        expected_name = 'Black bun'
        expected_price = 50.0
        # Act
        bun = Bun(name=expected_name, price=expected_price)
        # Assert
        assert bun.get_name() == expected_name, 'The Bun object name does not match the expected name.'
        assert bun.get_price() == pytest.approx(expected_price), 'Buns price does not match the expected price'
