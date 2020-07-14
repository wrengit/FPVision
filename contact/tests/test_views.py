from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from contact.models import SubscriptionList
from contact.forms import SubscriptionForm, ContactForm


class TestViews(TestCase):
    def test_redirect_after_subscribe_action(self):
        response = self.client.post(
            reverse("subscribe"), data={"email": "testemail@email.com", "next": "/"}
        )
        self.assertRedirects(response, "/")

    def test_add_new_email_to_subcription_list(self):
        test_email_on_list = SubscriptionList.objects.create(
            email="testemail1@email.com"
        )
        test_email_on_list.save()
        response = self.client.post(
            reverse("subscribe"),
            data={"email": "testemail2@email.com", "next": "/"},
            follow=True,
        )
        correct_message = "You've joined our mailing list!"
        self.assertEqual(str(list(response.context["messages"])[0]), correct_message)

    def test_add_existing_email_to_subcription_list(self):
        test_email_on_list = SubscriptionList.objects.create(
            email="testemail1@email.com"
        )
        test_email_on_list.save()
        response = self.client.post(
            reverse("subscribe"),
            data={"email": "testemail1@email.com", "next": "/"},
            follow=True,
        )
        correct_message = "You are aleady subscribed to the mailing list"
        self.assertEqual(str(list(response.context["messages"])[0]), correct_message)

    def test_contact_form_page_view(self):
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact/contact.html")
        self.assertEqual(response.status_code, 200)

    def test_contact_form_redirect_after_post(self):
        response = self.client.post(reverse("contact"),follow=True)
        self.assertTemplateUsed(response, "products/products.html")
        self.assertEqual(response.status_code, 200)

    def test_contact_form_post_not_authenticated(self):
        form_data = {
            "username":"testusername",
            "email":"testemail@email.com",
            "message":"a test message as a string"
        }
        form = ContactForm(form_data)
        response = self.client.post(reverse("contact"), form_data, follow=True)
        self.assertTrue(form.is_valid())
    
    def test_contact_form_post_authenticated(self):
        test_user = User.objects.create_user(
            username="test_user", password="jshSjSJ*£JS£S"
        )
        test_user.save()
        login = self.client.login(username="test_user", password="jshSjSJ*£JS£S")
        form_data = {
            "username":"testusername",
            "email":"testemail@email.com",
            "message":"a test message as a string"
        }
        form = ContactForm(form_data)
        response = self.client.post(reverse("contact"), form_data, follow=True)
        self.assertTrue(form.is_valid())

    def test_contact_form_get_authenticated(self):
        test_user = User.objects.create_user(
            username="test_user", password="jshSjSJ*£JS£S"
        )
        test_user.save()
        login = self.client.login(username="test_user", password="jshSjSJ*£JS£S")
        form_data = {
            "username":"testusername",
            "email":"testemail@email.com",
            "message":"a test message as a string"
        }
        form = ContactForm(form_data)
        response = self.client.get(reverse("contact"))
        self.assertTrue(form.is_valid())
        

   