from django.test import TestCase, RequestFactory
from products.models import Category, SubCategory, Product
from django.db.models import Q

"""
last two tests require refactoring to satisfy Coverage's demands
"""

class TestViews(TestCase):
    def test_search_view(self):
        response = self.client.get("/search/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/search.html")

    def test_search_by_product_name(self):
        test_category = Category.objects.create(name="test_category", slug="test-category")
        test_subcategory = SubCategory.objects.create(
            name="test_subcategory", slug="test-subcategory", category=test_category
        )
        test_product = Product.objects.create(
            name="test_product",
            slug="test-product",
            category=test_category,
            sub_category=test_subcategory,
            stock=1,
            price=1,
        )
        query = "test"
        products = Product.objects.all().filter(Q(name__contains=query))
        self.assertIn(test_product, products)
        
    def test_search_by_product_description(self):
        test_category = Category.objects.create(name="test_category", slug="test-category")
        test_subcategory = SubCategory.objects.create(
            name="test_subcategory", slug="test-subcategory", category=test_category
        )
        test_product = Product.objects.create(
            name="test_product",
            slug="test-product",
            description = "a test string",
            category=test_category,
            sub_category=test_subcategory,
            stock=1,
            price=1,
        )
        query = "string"
        products = Product.objects.all().filter(Q(description__contains=query))
        self.assertIn(test_product, products)
      
    
        
       
