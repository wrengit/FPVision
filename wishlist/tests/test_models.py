from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Category, SubCategory, Product
from wishlist.models import Wishlist, WishlistItem


class TestModels(TestCase):
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
        self.test_wishlist = Wishlist.objects.create(user=self.test_user)
        self.test_wishlist.save()

        self.test_wishlistitem = WishlistItem.objects.create(
            wishlist=self.test_wishlist, product=self.test_product, quantity=1
        )
        self.test_wishlistitem.save()

    def test_WishListItem_returns_string(self):
        self.assertEqual(
            str(self.test_wishlistitem), f"{self.test_product.name} on wishlist"
        )

