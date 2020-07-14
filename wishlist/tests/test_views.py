from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from products.models import Category, SubCategory, Product
from django.urls import reverse
from wishlist.models import Wishlist, WishlistItem


class TestViews(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="test_user", password="jshSjSJ*£JS£S"
        )
        self.test_user.save()

        test_category, created = Category.objects.get_or_create(
            name="test_category", slug="test-category"
        )
        test_category.save()
        test_subcategory, created = SubCategory.objects.get_or_create(
            name="test_subcategory", slug="test-subcategory", category=test_category,
        )
        test_subcategory.save()
        self.test_product, created = Product.objects.get_or_create(
            name="test_product",
            slug="test-product",
            description="string",
            category=test_category,
            sub_category=test_subcategory,
            stock=1,
            price=1,
        )
        self.test_product.save()

        self.login = self.client.login(username="test_user", password="jshSjSJ*£JS£S")

    def test_wishlist_main_view(self):
        self.login
        response = self.client.get(reverse("view_wishlist"), follow=True)
        self.assertTemplateUsed(response, "profiles/wishlist.html")
        self.assertEqual(response.status_code, 200)

