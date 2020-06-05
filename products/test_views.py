from django.test import TestCase
from .models import Category, SubCategory, Product


class TestViews(TestCase):
    def test_all_products_view(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_category_product_view(self):
        test_category = Category.objects.create(
            name="test_category", slug="test-category"
        )
        response = self.client.get("/products/test-category/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_subcategory_product_view(self):
        test_category = Category.objects.create(
            name="test_category", slug="test-category"
        )
        test_subcategory = SubCategory.objects.create(
            name="test_subcategory", slug="test-subcategory", category=test_category
        )

        response = self.client.get("/products/test-category/test-subcategory/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_product_details_view(self):
        test_category = Category.objects.create(
            name="test_category", slug="test-category"
        )
        test_subcategory = SubCategory.objects.create(
            name="test_subcategory", slug="test-subcategory", category=test_category
        )
        test_product = Product.objects.create(
            name="test_product",
            slug="test-product",
            category=test_category,
            sub_category=test_subcategory,
            stock=10,
            price=10,
            available=True,
            sku = 1234567890,
        )
        url = test_product.get_url()
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_details.html")
