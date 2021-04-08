from django.test import TestCase

from dj_emailauth.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            password="password", email="email@email.com"
        )
        self.user.full_clean()

        self.superuser = User.objects.create_superuser(
            password="password", email="superuser@email.com"
        )
        self.superuser.full_clean()

    def test_string_representation(self):
        self.assertEqual(str(self.user), "email@email.com")
        self.assertEqual(str(self.superuser), "superuser@email.com")

    def test_superuser(self):
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)
        self.assertTrue(self.superuser.is_active)

    def test_user(self):
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(self.user.is_active)

    def test_email_normalize(self):
        user = User.objects.create_user(
            password="password", email="MYEMAIL@EXAMPLE.cOm"
        )
        self.assertEqual(str(user), "MYEMAIL@example.com")
