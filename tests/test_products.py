# tests/test_products.py
import pytest
from src.products import Product, Category


@pytest.fixture
def sample_product():
    """Фикстура для создания тестового продукта."""
    return Product("Test Product", "Test Description", 100.0, 5)


@pytest.fixture
def sample_category(sample_product):
    """Фикстура для тестовой категории с одним продуктом."""
    return Category("Test Category", "Test Category Description", [sample_product])


class TestProduct:
    """Тесты для класса Product."""

    def test_product_initialization(self, sample_product):
        """Тест инициализации продукта."""
        assert sample_product.name == "Test Product"
        assert sample_product.description == "Test Description"
        assert sample_product.price == 100.0
        assert sample_product.quantity == 5


class TestCategory:
    """Тесты для класса Category."""

    def test_category_initialization(self, sample_category, sample_product):
        """Тест инициализации категории."""
        assert sample_category.name == "Test Category"
        assert sample_category.description == "Test Category Description"
        assert len(sample_category.products) == 1
        assert sample_category.products[0].name == "Test Product"

    def test_category_count(self):
        """Тест подсчета количества категорий."""
        initial_count = Category.category_count
        _ = Category("Temp", "Temp", [])  # Используем _ для неиспользуемой переменной
        assert Category.category_count == initial_count + 1
        Category.category_count -= 1

    def test_product_count(self, sample_product):
        """Тест подсчета количества продуктов."""
        initial_count = Category.product_count
        _ = Category("Temp", "Temp", [sample_product, sample_product])  # Используем _
        assert Category.product_count == initial_count + 2
        Category.category_count -= 1
        Category.product_count -= 2

    def test_empty_category(self):
        """Тест создания категории без продуктов."""
        _ = Category("Empty", "Empty", [])  # Используем _
        assert Category.product_count == 0
        Category.category_count -= 1
