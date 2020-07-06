from django.test import TestCase
from .models import Category, SubCategory, Product


class TestViews(TestCase):
    def setUp(self):
        Category.objects.create(name="test_category", slug="test-category")
        self.test_category = Category.objects.get(name="test_category")
        SubCategory.objects.create(
            name="test_subcategory",
            slug="test-subcategory",
            category=self.test_category,
        )
        self.test_subcategory = SubCategory.objects.get(name="test_subcategory")
        self.test_product = Product.objects.create(
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

    def test_all_products_view(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_category_product_view(self):
        response = self.client.get("/products/test-category/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_subcategory_product_view(self):
        response = self.client.get("/products/test-category/test-subcategory/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_product_details_view(self):
        url = self.test_product.get_url()
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_details.html")
