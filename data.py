"""
Тестовые данные для тестов классов Bun и Burger
"""

# Данные для тестов булочек (Bun)
BUN_NAMES = [
    'Булочка 1',
    'Булочка 2',
    'Булочка 3',
]

BUN_PRICES = [
    1255.0,
    988.0,
    100.0,
    200.5,
    0.0,
]

# Константы для тестов Bun
BUN_DEFAULT_NAME = 'Самая вкусная булка'
BUN_DEFAULT_PRICE = 100.0


# Данные для тестов ингредиентов
INGREDIENT_TYPES = {
    'SAUCE': 'SAUCE',
    'FILLING': 'FILLING',
}

INGREDIENT_NAMES = [
    'Соус',
    'Начинка',
    'Соус2',
]

INGREDIENT_PRICES = [
    50.0,
    100.0,
    60.0,
]

# Константы для тестов Ingredient
INGREDIENT_DEFAULT_TYPE = 'SAUCE'
INGREDIENT_DEFAULT_NAME = 'Соус'
INGREDIENT_DEFAULT_PRICE = 50.0

# Данные для параметризованных тестов
PRICE_TEST_CASES = [
    (100.0, 50.0, 250.0),
    (200.0, 100.0, 500.0),
    (50.0, 25.0, 125.0),
]

