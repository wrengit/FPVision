from django.test import TestCase
from products.models import Product, SubCategory, Category
from django.test.client import Client


class TestViews(TestCase):

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
        c = Client()

    def tearDown(self):
        del self.test_category
        del self.test_subcategory
        del self.test_product


    def test_view_basket_page(self):
        response = self.client.get("/basket/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "basket/basket.html")


