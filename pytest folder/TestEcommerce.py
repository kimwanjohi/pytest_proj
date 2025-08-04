# test_ecommerce.py

import pytest
from ecommerce import Product, ShoppingCart, OrderProcessor


@pytest.fixture
def sample_products():
    p1 = Product("Laptop", 1000, 10)
    p2 = Product("Phone", 500, 5)
    return p1, p2

def test_add_and_remove_items(sample_products):
    p1, p2 = sample_products
    cart = ShoppingCart()
    cart.add_item(p1, 2)
    cart.add_item(p2, 1)

    assert cart.calculate_total() == 1000*2 + 500*1

    cart.remove_item(p1)
    assert cart.calculate_total() == 500


def test_add_item_insufficient_stock(sample_products):
    p1, _ = sample_products
    cart = ShoppingCart()
    with pytest.raises(ValueError, match="Insufficient stock"):
        cart.add_item(p1, 20)  # More than available


def test_place_order_reduces_stock(sample_products):
    p1, p2 = sample_products
    cart = ShoppingCart()
    cart.add_item(p1, 2)
    cart.add_item(p2, 1)

    processor = OrderProcessor()
    result = processor.place_order(cart)

    assert "order_id" in result
    assert result["total"] == 1000*2 + 500*1
    assert p1.stock == 8
    assert p2.stock == 4


def test_invalid_quantity_add():
    p = Product("Book", 50, 10)
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item(p, 0)
