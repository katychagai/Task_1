
from ingredient import Ingredient
from data import THREE_INGREDIENTS_DATA

#Вспомогательные функции для создания тестовых объектов
def get_three_ingredients():
    return [Ingredient(ingredient_type, name, price) 
            for ingredient_type, name, price in THREE_INGREDIENTS_DATA]

