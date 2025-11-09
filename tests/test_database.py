import pytest
from database import Database


class TestDatabase:

    #Тест: метод available_buns возвращает 3 булочки
    def test_available_buns_returns_three_buns(self):
        database = Database()
        result = database.available_buns()

        assert len(result) == 3

    #Тест: метод available_buns возвращает тот же список, что и buns
    def test_available_buns_returns_same_list_as_buns(self):
        database = Database()

        assert database.available_buns() is database.buns

    #Тест: метод available_ingredients возвращает 6 ингредиентов
    def test_available_ingredients_returns_six_ingredients(self):
        database = Database()
        result = database.available_ingredients()

        assert len(result) == 6

    #Тест: метод available_ingredients возвращает тот же список, что и ingredients
    def test_available_ingredients_returns_same_list_as_ingredients(self):
        database = Database()

        assert database.available_ingredients() is database.ingredients

