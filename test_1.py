import pytest
from order_calculator import OrderCalculator

def test_basic_order():
    calc = OrderCalculator([
        {"name": "Товар 1", "price": 20.0, "quantity": 1},
        {"name": "Товар 2", "price": 30.0, "quantity": 1}
    ])
    total = calc.calculate_total()
    assert round(total, 2) == 57.5  # с учётом налога и доставки

def test_basic_order_1():
    calc = OrderCalculator([
        {"name": "Товар 1", "price": 20.0, "quantity": 1},
        {"name": "Товар 2", "price": 30.0, "quantity": 1}
    ])
    total = calc.calculate_total()
    assert not round(total, 2) == 157.5  # с учётом налога


def test_discount_at_threshold():
    # Создаем заказ с общей стоимостью ровно 10000 (порог скидки)
    items = [
        {"name": "Товар 1", "price": 5000, "quantity": 2},
    ]
    calculator = OrderCalculator(items)

    # Ожидаемый расчет:
    # 1. Сумма без скидки: 5000 * 2 = 10000
    # 2. Применяется скидка 10%: 10000 * 0.9 = 9000
    # 3. Добавляется налог 15%: 9000 * 1.15 = 10350.0
    expected_total = 10350.0
    assert calculator.calculate_total() == expected_total


def test_tax_calculation_without_discount():
    #Проверка расчета налога без применения скидки
    items = [
        {"name": "Товар 1", "price": 1000, "quantity": 2},
        {"name": "Товар 2", "price": 500, "quantity": 1},
    ]

    calculator = OrderCalculator(items)

    # Ожидаемый расчет:
    # 1. Сумма без скидки: 2000 + 500 = 2500
    # 2. Скидка не применяется
    # 3. Налог 15%: 2500 * 1.15 = 2875.0
    expected_total = 2875.0

    assert calculator.calculate_total() == expected_total


def test_tax_calculation_with_discount():
    #Проверка расчета налога с применением скидки
    items = [
        {"name": "Дорогой товар", "price": 6000, "quantity": 2},
    ]

    calculator = OrderCalculator(items)

    # Ожидаемый расчет:
    # 1. Сумма без скидки: 12000
    # 2. Скидка 10%: 12000 * 0.9 = 10800
    # 3. Налог 15%: 10800 * 1.15 = 12420.0
    expected_total = 12420.0

    assert calculator.calculate_total() == expected_total
