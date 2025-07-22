from typing import List, Dict
import pytest
class OrderCalculator:
    TAX_RATE = 0.15  # 15% налог
    DISCOUNT_THRESHOLD = 10000
    DISCOUNT_RATE = 0.1  # 10% скидка

    def __init__(self, items: List[Dict[str, float]]):
        """
        items: список словарей с полями:
        - 'name': название товара
        - 'price': цена за единицу
        - 'quantity': количество
        """
        self.items = items

    def calculate_total(self) -> float:
        total = 0
        for item in self.items:
            if item['price'] < 0 or item['quantity'] < 0:
                raise ValueError("Цена и количество не могут быть отрицательными.")
            total += item['price'] * item['quantity']

        if total >= self.DISCOUNT_THRESHOLD:
            total *= (1 - self.DISCOUNT_RATE)

        total *= (1 + self.TAX_RATE)

        return round(total, 2)

    def most_expensive_item(self) -> str:
        if not self.items:
            raise ValueError("Список товаров пуст.")
        return max(self.items, key=lambda item: item['price'])['name']
