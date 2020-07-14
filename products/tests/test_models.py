from django.test import TestCase
from products.models import Category, SubCategory, Product


class TestModels(TestCase):
    def setUp(self):

        self.test_category, created = Category.objects.get_or_create(
            name="test_category", slug="test-category"
        )

        self.test_subcategory, created = SubCategory.objects.get_or_create(
            name="test_subcategory",
            slug="test-subcategory",
            category=self.test_category,
        )
        self.test_product, created = Product.objects.get_or_create(
            name="test_product",
            slug="test-product",
            description="string",
            category=self.test_category,
            sub_category=self.test_subcategory,
            stock=1,
            price=1,
        )

    def tearDown(self):
        del self.test_category
        del self.test_subcategory
        del self.test_product

    def test_str_to_return_name_for_category(self):
        self.assertEqual(str(self.test_category), self.test_category.name)

    def test_str_to_return_name_for_subcategory(self):
        correct_name = (
            self.test_subcategory.category.name + " --> " + self.test_subcategory.name
        )
        self.assertEqual(str(self.test_subcategory), correct_name)

    def test_str_to_return_name_for_Product(self):
        self.assertEqual(str(self.test_product), self.test_product.name)
