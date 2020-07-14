from django.test import TestCase
from checkout.models import Order, OrderLineItem
from products.models import Category, SubCategory, Product


class TestModels(TestCase):
    def setUp(self):
        self.test_order = Order.objects.create(
            full_name="testname",
            email="testemail@email.com",
            phone_number="09876",
            country="GB",
            postcode="hh67hf",
            post_town="testtown",
            address_1="123 address",
        )
        self.test_order.save()

        test_category = Category.objects.create(
            name="test_category", slug="test-category"
        )

        test_subcategory = SubCategory.objects.create(
            name="test_subcategory", slug="test-subcategory", category=test_category,
        )
        self.test_product = Product.objects.create(
            name="test_product",
            slug="test-product",
            description="string",
            category=test_category,
            sub_category=test_subcategory,
            stock=1,
            price=1,
        )
        self.test_product.save()

    def test_Order_model_returns_string_order_number(self):
        self.assertEqual(str(self.test_order), self.test_order.order_number)

    def test_OrderLineItem_model_returns_string(self):
        test_order_line_item = OrderLineItem.objects.create(
            order=self.test_order, product=self.test_product, quantity=1
        )
        self.assertEqual(
            str(test_order_line_item),
            f"SKU {self.test_product.sku} on order {self.test_order.order_number}",
        )

