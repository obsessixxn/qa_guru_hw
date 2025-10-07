"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework6.models import Product, Cart


@pytest.fixture
def product() -> Product:
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def product_milk() -> Product:
    return Product("milk", 100, "This is a milk", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity_equals(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity)

    def test_product_check_quantity_negative(self, product):
        # TODO напишите проверки на метод check_quantity
        assert not product.check_quantity(product.quantity + 1)

    def test_product_check_quantity_less(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity - 1)

    def test_product_buy_500(self, product):
        buy_quantity = 500
        products = product.quantity
        product.buy(buy_quantity)
        assert product.quantity == products - buy_quantity

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            buy_quantity = product.quantity + 1
            product.buy(buy_quantity)


@pytest.fixture(scope="function")
def cart() -> Cart:
    return Cart()


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, cart, product):
        cart.add_product(product, 1000)
        assert cart.products[product] == 1000

    def test_cart_add_product_negative(self, cart, product):
        with pytest.raises(ValueError):
            cart.add_product(product, product.quantity + 1)

    def test_cart_add_product_zero(self, cart, product):
        with pytest.raises(ValueError):
            cart.add_product(product, product.quantity - product.quantity)

    def test_cart_remove_all_product(self, cart, product):
        cart.add_product(product, 100)
        cart.remove_product(product, 100)
        assert len(cart.products) == 0

    def test_cart_remove_few_product(self, cart, product):
        cart.add_product(product, 100)
        cart.remove_product(product, 10)
        assert cart.products[product] == 90

    def test_cart_remove_product_negative(self, cart, product):
        with pytest.raises(ValueError):
            cart.remove_product(product, 100)

    def test_get_total_price(self, cart, product):
        product_count = 100
        cart.add_product(product, 100)
        cart.get_total_price()
        assert cart.get_total_price() == product.price * product_count

    def test_clear_one_product(self, cart, product):
        cart.add_product(product, 100)
        cart.clear()
        assert len(cart.products) == 0

    def test_clear_empty_cart(self, cart):
        with pytest.raises(ValueError):
            cart.clear()

    def test_cart_buy(self, cart, product):
        product_quantity = product.quantity
        quantity_to_buy = 1000
        cart.add_product(product, quantity_to_buy)
        cart.buy()
        assert len(cart.products) == 0 and product.quantity == product_quantity - quantity_to_buy

    def test_cart_buy_negative(self, cart, product):
        with pytest.raises(ValueError):
            quantity_to_buy = 2000
            cart.add_product(product, quantity_to_buy)
            cart.buy()

    def test_cart_buy_zero(self, cart, product):
        with pytest.raises(ValueError):
            quantity_to_buy = 0
            cart.add_product(product, quantity_to_buy)
            cart.buy()

