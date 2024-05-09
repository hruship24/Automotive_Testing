import pytest
from app.cart import ShoppingCart


@pytest.fixture
def shopping_cart():
    cart = ShoppingCart()
    yield cart
    # Teardown: Clean up the shopping cart after each test
    cart.items = {}


@pytest.fixture
def sample_products():
    return {
        "product1": 10,  # Price for product1 is $10
        "product2": 20,  # Price for product2 is $20
        "product3": 30   # Price for product3 is $30
    }


def test_add_item(shopping_cart):
    shopping_cart = shopping_cart
    actual_result=shopping_cart.add_item("product1", 1)
    assert actual_result== {"product1": 1}


def test_remove_item(shopping_cart):
    shopping_cart.items = {"product2": 2}
    shopping_cart.remove_item("product2", 1)
    assert shopping_cart.items == {"product2": 1}


def test_update_quantity(shopping_cart):
    shopping_cart.items = {"product3": 1}
    shopping_cart.update_quantity("product3", 2)
    assert shopping_cart.items == {"product3": 2}


def test_calculate_subtotal(shopping_cart, sample_products):
    shopping_cart.items = {"product1": 2, "product2": 1}
    # Total price for product1: 2 * 10 = $20
    # Total price for product2: 1 * 20 = $20
    # Subtotal = 20 + 20 = $40
    assert shopping_cart.calculate_subtotal(sample_products) == 40
