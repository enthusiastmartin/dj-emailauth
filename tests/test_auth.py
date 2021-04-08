from django.contrib.auth import authenticate
from django.test import TestCase

from dj_emailauth.models import User


class AuthenticateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            password="password", email="email@email.com", is_active=True
        )
        self.user.full_clean()

    def test_email_authenticate(self):
        user = authenticate(email="email@email.com", password="password")

        self.assertIsNotNone(user)

    def test_invalid_credentials(self):
        user = authenticate(email="email@email.com", password="passwordinvalid")
        self.assertIsNone(user)

        user = authenticate(email="invalidemail@email.com", password="password")
        self.assertIsNone(user)

    def test_username_auth(self):
        """ Test if username auth is not possible """
        user = authenticate(username="someusername", password="password")

        self.assertIsNone(user)
