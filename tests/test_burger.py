import pytest
from unittest.mock import Mock
from bun import Bun
from ingredient import Ingredient
from burger import Burger
from data import (
    BUN_NAMES, 
    BUN_PRICES, 
    PRICE_TEST_CASES, 
    INGREDIENT_TYPES, 
    INGREDIENT_NAMES, 
    INGREDIENT_PRICES,
    BUN_DEFAULT_NAME,
    BUN_DEFAULT_PRICE
)


class TestBurger:

    #Тест: метод set_buns устанавливает булочку
    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = Bun(BUN_DEFAULT_NAME, BUN_DEFAULT_PRICE)
        burger.set_buns(bun)

        assert burger.bun == bun

    #Тест: метод set_buns устанавливает имя булочки
    @pytest.mark.parametrize('name', BUN_NAMES[:3])
    def test_set_buns_sets_bun_name(self, name):
        burger = Burger()
        bun = Bun(name, BUN_DEFAULT_PRICE)
        burger.set_buns(bun)

        assert burger.bun.get_name() == name

    #Тест: метод set_buns устанавливает цену булочки
    @pytest.mark.parametrize('price', BUN_PRICES[:3])
    def test_set_buns_sets_bun_price(self, price):
        burger = Burger()
        bun = Bun(BUN_DEFAULT_NAME, price)
        burger.set_buns(bun)

        assert burger.bun.get_price() == price

    #Тест: метод add_ingredient добавляет ингредиент в список
    def test_add_ingredient_adds_ingredient_to_list(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPES['SAUCE'], INGREDIENT_NAMES[0], INGREDIENT_PRICES[0])
        burger.add_ingredient(ingredient)

        assert burger.ingredients[0] == ingredient

    #Тест: метод add_ingredient добавляет ингредиент на правильную позицию
    @pytest.mark.parametrize('position,ingredient_index', [
        (0, 0),  # Первый ингредиент на позиции 0
        (1, 1),  # Второй ингредиент на позиции 1
    ])
    def test_add_ingredient_adds_ingredient_to_position(self, position, ingredient_index, three_ingredients):
        burger = Burger()
        ingredient1, ingredient2 = three_ingredients[0], three_ingredients[1]
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        assert burger.ingredients[position] == three_ingredients[ingredient_index]

    #Тест: метод remove_ingredient удаляет правильный ингредиент
    def test_remove_ingredient_removes_correct_ingredient(self, three_ingredients):
        burger = Burger()
        ingredient1, ingredient2 = three_ingredients[0], three_ingredients[1]
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)

        assert burger.ingredients[0] == ingredient2

    #Тест: метод move_ingredient перемещает ингредиент на указанную позицию
    @pytest.mark.parametrize('position,expected_ingredient_index', [
        (0, 1),  # После move_ingredient(0, 2) на позиции 0 должен быть ingredient2 (индекс 1)
        (1, 2),  # На позиции 1 должен быть ingredient3 (индекс 2)
        (2, 0),  # На позиции 2 должен быть ingredient1 (индекс 0)
    ])
    def test_move_ingredient_moves_to_position(self, position, expected_ingredient_index, three_ingredients):
        burger = Burger()
        ingredient1, ingredient2, ingredient3 = three_ingredients
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(0, 2)

        assert burger.ingredients[position] == three_ingredients[expected_ingredient_index]

    #Тест: метод get_price возвращает цену булочки умноженную на 2 без ингредиентов
    def test_get_price_returns_bun_price_times_two_without_ingredients(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        result = burger.get_price()
        
        assert result == 200.0

    #Тест: метод get_price вызывает ingredient.get_price() для первого ингредиента
    def test_get_price_calls_first_ingredient_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0
        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 50.0
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 75.0
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.get_price()
        
        mock_ingredient1.get_price.assert_called_once()

    #Тест: метод get_price вызывает ingredient.get_price() для второго ингредиента
    def test_get_price_calls_second_ingredient_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0
        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 50.0
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 75.0
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.get_price()
        
        mock_ingredient2.get_price.assert_called_once()

    #Тест: метод get_price правильно рассчитывает общую цену
    @pytest.mark.parametrize('bun_price,ingredient_price,expected_price', PRICE_TEST_CASES)
    def test_get_price_calculates_correct_total(self, bun_price, ingredient_price, expected_price):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ingredient_price
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        result = burger.get_price()
        
        assert result == expected_price

    #Тест: метод get_price возвращает float
    def test_get_price_returns_float_type(self):
        burger = Burger()
        bun = Bun(BUN_DEFAULT_NAME, BUN_DEFAULT_PRICE)
        burger.set_buns(bun)
        result = burger.get_price()
        assert isinstance(result, float)

    #Тест: метод get_receipt возвращает строку
    def test_get_receipt_returns_string_type(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        result = burger.get_receipt()
        
        assert isinstance(result, str)

    #Тест: метод get_receipt содержит название булочки
    def test_get_receipt_contains_bun_name(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        
        assert 'Test Bun' in receipt

    #Тест: метод get_receipt содержит тип ингредиента
    def test_get_receipt_contains_ingredient_type(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        
        assert 'sauce' in receipt.lower()

    #Тест: метод get_receipt содержит название ингредиента
    def test_get_receipt_contains_ingredient_name(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        
        assert 'Test Sauce' in receipt

    #Тест: метод get_receipt содержит метку цены
    def test_get_receipt_contains_price_label(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        
        assert 'Price:' in receipt

    #Тест: метод get_receipt содержит значение цены
    def test_get_receipt_contains_price_value(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        
        assert '200.0' in receipt
