import pytest
from order_calculator import OrderCalculator


def test_basic_order():
    calc = OrderCalculator([
        {"name": "Товар 1", "price": 20.0, "quantity": 1},
        {"name": "Товар 2", "price": 30.0, "quantity": 1}
    ])
    total = calc.calculate_total()
    assert round(total, 2) == 57.5  # с учётом налога

def test_basic_order_1():
    calc = OrderCalculator([
        {"name": "Товар 1", "price": 20.0, "quantity": 1},
        {"name": "Товар 2", "price": 30.0, "quantity": 1}
    ])
    total = calc.calculate_total()
    assert not round(total, 2) == 157.5  # с учётом налога
