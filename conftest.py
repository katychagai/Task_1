import pytest
from unittest.mock import Mock
from helpers import get_three_ingredients


@pytest.fixture
def three_ingredients():
    return get_three_ingredients()


#Фикстура для создания mock булочки для тестов get_receipt
@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Test Bun'
    mock_bun.get_price.return_value = 100.0
    return mock_bun


#Фикстура для создания mock ингредиента для тестов get_receipt
@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = 'SAUCE'
    mock_ingredient.get_name.return_value = 'Test Sauce'
    mock_ingredient.get_price.return_value = 50.0
    return mock_ingredient

