# ecommerce.py

import uuid

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            raise ValueError("Not enough stock.")

    def increase_stock(self, quantity):
        self.stock += quantity


class ShoppingCart:
    def __init__(self):
        self.items = {}  # key: product, value: quantity

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if product.stock < quantity:
            raise ValueError("Insufficient stock.")
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]

    def calculate_total(self):
        return sum(product.price * qty for product, qty in self.items.items())


class OrderProcessor:
    def place_order(self, shopping_cart):
        for product, qty in shopping_cart.items.items():
            product.reduce_stock(qty)
        order_id = str(uuid.uuid4())
        return {"order_id": order_id, "total": shopping_cart.calculate_total()}
