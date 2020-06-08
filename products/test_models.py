from django.test import TestCase
from .models import *

class TestModels(TestCase):
    def test_str_to_return_name_for_category(self):
        test_category = Category.objects.create(name="test_category")
        self.assertEqual(str(test_category), test_category.name)

    def test_str_to_return_name_for_subcategory(self):
        test_category = Category.objects.create(name="test_category")
        test_subcategory = SubCategory.objects.create(name="test_subcategory", category = test_category, )
        correct_name = test_subcategory.category.name + " --> " + test_subcategory.name
        self.assertEqual(str(test_subcategory), correct_name)

    def test_str_to_return_name_for_Product(self):
        test_product = Product.objects.create(name="test_product", stock=1, price=1)
        self.assertEqual(str(test_product), test_product.name)