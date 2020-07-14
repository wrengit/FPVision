from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile


class TestModels(TestCase):
    def test_UserProfile_model_returns_string_name(self):
        test_user = User.objects.create_user(
            username="test_user", password="jshSjSJ*£JS£S"
        )
        test_user.save()
        self.assertEqual(str(test_user.userprofile), test_user.username)
