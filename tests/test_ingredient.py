import pytest
from ingredient import Ingredient
from data import (
    INGREDIENT_TYPES,
    INGREDIENT_NAMES,
    INGREDIENT_PRICES,
    INGREDIENT_DEFAULT_TYPE,
    INGREDIENT_DEFAULT_NAME,
    INGREDIENT_DEFAULT_PRICE,
)


class TestIngredient:
    

    #Тест: метод get_type возвращает корректное значение
    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPES['SAUCE'], INGREDIENT_TYPES['FILLING']])
    def test_get_type_returns_correct_value(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, INGREDIENT_DEFAULT_NAME, INGREDIENT_DEFAULT_PRICE)
        result = ingredient.get_type()

        assert result == ingredient_type

    #Тест: метод get_type возвращает строку
    def test_get_type_returns_string_type(self):
        ingredient = Ingredient(INGREDIENT_DEFAULT_TYPE, INGREDIENT_DEFAULT_NAME, INGREDIENT_DEFAULT_PRICE)
        result = ingredient.get_type()

        assert isinstance(result, str)

    #Тест: метод get_name возвращает корректное значение
    @pytest.mark.parametrize('name', INGREDIENT_NAMES)
    def test_get_name_returns_correct_value(self, name):
        ingredient = Ingredient(INGREDIENT_DEFAULT_TYPE, name, INGREDIENT_DEFAULT_PRICE)
        result = ingredient.get_name()

        assert result == name

    #Тест: метод get_name возвращает строку
    def test_get_name_returns_string_type(self):
        ingredient = Ingredient(INGREDIENT_DEFAULT_TYPE, INGREDIENT_DEFAULT_NAME, INGREDIENT_DEFAULT_PRICE)
        result = ingredient.get_name()

        assert isinstance(result, str)

    #Тест: метод get_price возвращает корректное значение
    @pytest.mark.parametrize('price', INGREDIENT_PRICES)
    def test_get_price_returns_correct_value(self, price):
        ingredient = Ingredient(INGREDIENT_DEFAULT_TYPE, INGREDIENT_DEFAULT_NAME, price)
        result = ingredient.get_price()

        assert result == price

    #Тест: метод get_price возвращает float
    def test_get_price_returns_float_type(self):
        ingredient = Ingredient(INGREDIENT_DEFAULT_TYPE, INGREDIENT_DEFAULT_NAME, INGREDIENT_DEFAULT_PRICE)
        result = ingredient.get_price()

        assert isinstance(result, float)


