from django.test import TestCase
from contact.models import ContactList, SubscriptionList


class TestModels(TestCase):
    def test_ContactList_returns_string_name(self):
        test_contact_list = ContactList.objects.create(
            username="testusername", email="testemail@email.com", message="testmessage"
        )
        test_contact_list.save()
        self.assertEqual(str(test_contact_list), "testusername")

    def test_SubscriptionList_returns_string_name(self):
        test_subscription_list = SubscriptionList.objects.create(
            email="testemail@email.com"
        )
        test_subscription_list.save()
        self.assertEqual(str(test_subscription_list), "testemail@email.com")
