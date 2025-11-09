import pytest
from bun import Bun
from data import (
    BUN_NAMES,
    BUN_PRICES,
    BUN_DEFAULT_NAME,
    BUN_DEFAULT_PRICE,
)


class TestBun:

    #Тест: метод get_name возвращает корректное значение
    @pytest.mark.parametrize('name', BUN_NAMES)
    def test_get_name_returns_correct_value(self, name):
        bun = Bun(name, BUN_DEFAULT_PRICE)
        result = bun.get_name()
        
        assert result == name

    #Тест: метод get_name возвращает строку
    def test_get_name_returns_string_type(self):
        bun = Bun(BUN_DEFAULT_NAME, BUN_DEFAULT_PRICE)
        result = bun.get_name()

        assert isinstance(result, str)

    #Тест: метод get_price возвращает корректное значение
    @pytest.mark.parametrize('price', BUN_PRICES)
    def test_get_price_returns_correct_value(self, price):
        bun = Bun(BUN_DEFAULT_NAME, price)
        result = bun.get_price()

        assert result == price

    #Тест: метод get_price возвращает float
    def test_get_price_returns_float_type(self):
        bun = Bun(BUN_DEFAULT_NAME, BUN_DEFAULT_PRICE)
        result = bun.get_price()

        assert isinstance(result, float)
