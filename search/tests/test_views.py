from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.messages import get_messages
from products.models import Category, SubCategory, Product
from django.db.models import Q


class TestViews(TestCase):
    def setUp(self):

        self.test_category, created = Category.objects.get_or_create(
            name="test category", slug="test-category"
        )

        self.test_subcategory, created = SubCategory.objects.get_or_create(
            name="test subcategory",
            slug="test-subcategory",
            category=self.test_category,
        )
        self.test_product, created = Product.objects.get_or_create(
            name="test product",
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

    def test_search_view(self):
        response = self.client.get("/search/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search/search.html")

    def test_search_by_product_name(self):
        url = "{url}?{filter}={value}".format(
            url=reverse("search_result"), filter="q", value="test"
        )
        query = "test"
        response = self.client.get(url)
        test_products = Product.objects.all().filter(Q(name__contains=query))
        self.assertQuerysetEqual(
            response.context["products"], test_products, transform=lambda x: x
        )

    def test_search_by_product_description(self):
        url = "{url}?{filter}={value}".format(
            url=reverse("search_result"), filter="q", value="string"
        )
        query = "string"
        response = self.client.get(url)
        test_products = Product.objects.all().filter(Q(description__contains=query))
        self.assertQuerysetEqual(
            response.context["products"], test_products, transform=lambda x: x
        )

    def test_correct_error_message(self):
        url = "{url}?{filter}={value}".format(
            url=reverse("search_result"), filter="q", value=""
        )
        response = self.client.get(url)
        test_messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Please enter a search criteria", test_messages)

    def test_js_search_by_product_name(self):
        url = "{url}?{filter}={value}".format(
            url=reverse("js_search"), filter="q", value="test"
        )
        response = self.client.get(url)
        self.assertJSONEqual(
            response.content.decode("utf8"),
            [
                {
                    "name": "test product",
                    "price": "1.00",
                    "category": "test category",
                    "sub_category": "test subcategory",
                    "image": "defaults/default_product.jpg",
                    "id": 1,
                    "full_slug": "test-category/test-subcategory/test-product",
                    "stock": 1,
                }
            ],
        )
