from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'avtsur@gmail.com'
        password = 'Stam1234'
        user = get_user_model().objects.create_user(email = email,
        password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'aaa@AVRAM.Com'
        user = get_user_model().objects.create_user(email, 'stam122')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
        'test@londonappdev.com',
        'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
