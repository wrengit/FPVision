from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile
from products.models import Category, SubCategory, Product
from profiles.forms import UserProfileForm, UserForm


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
        test_product, created = Product.objects.get_or_create(
            name="test_product",
            slug="test-product",
            description="string",
            category=test_category,
            sub_category=test_subcategory,
            stock=1,
            price=1,
        )
        test_product.save()
        self.test_order = Order.objects.create(
            full_name="test_user",
            email="test@email.com",
            phone_number="12345",
            country="UK",
            post_town="test_town",
            address_1="123 street",
        )
        self.test_order.save()
        test_line_item = OrderLineItem.objects.create(
            order=self.test_order, product=test_product, quantity=1
        )
        test_line_item.save()

    def test_redirect_if_user_not_logged_in(self):
        response = self.client.get(reverse("my_account"))
        self.assertRedirects(response, "/accounts/login/?next=/profile/")

    def test_logged_to_access_main_profile_view(self):
        login = self.client.login(username="test_user", password="jshSjSJ*£JS£S")
        response = self.client.get(reverse("my_account"))
        self.assertEqual(str(response.context["user"]), "test_user")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/my_account.html")

    def test_view_order_history_with_no_orders(self):
        login = self.client.login(username="test_user", password="jshSjSJ*£JS£S")
        response = self.client.get(reverse("order_history"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/order_history.html")

    def test_view_order_history_with_previous_orders(self):
        login = self.client.login(username="test_user", password="jshSjSJ*£JS£S")
        response = self.client.get(
            reverse("order_history_order", args=[self.test_order.order_number])
        )
        self.assertTemplateUsed(response, "checkout/checkout_success.html")
        self.assertEqual(response.status_code, 200)

    def test_update_profile_address_view(self):
        login = self.client.login(username="test_user", password="jshSjSJ*£JS£S")
        response = self.client.get(reverse("update_address"))
        self.assertTemplateUsed(response, "profiles/update_address.html")
        self.assertEqual(response.status_code, 200)

    def test_update_address_form(self):
        login = self.client.login(username="test_user", password="jshSjSJ*£JS£S")
        user = self.test_user
        response = self.client.post(reverse("update_address"))
        form_data = {"default_phone_number": "09876", "user": user.id}
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_update_account_details_view(self):
        login = self.client.login(username="test_user", password="jshSjSJ*£JS£S")
        response = self.client.get(reverse("update_account_details"))
        self.assertTemplateUsed(response, "profiles/update_account_details.html")
        self.assertEqual(response.status_code, 200)

    def test_update_account_form(self):
        login = self.client.login(username="test_user", password="jshSjSJ*£JS£S")
        user = self.test_user
        response = self.client.post(reverse("update_account_details"))
        form_data = {"username": "updated_username"}
        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid())

