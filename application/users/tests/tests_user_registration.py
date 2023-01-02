from httpx import Response

from application.users.models import User
from extra_libs.testing import FastApiTestCase


# Create your tests here.
class RegisterUserTestCase(FastApiTestCase):

    def test_register_user(self):
        response = self.fast_api_client.post(
            url="/fast-api/users",
            json={
                'email': 'user@email.com',
                'first_name': 'John',
                'last_name': 'Doe',
                'phone': '123456789',
                'password': 'random_not_secure_password',
                'repeated_password': 'random_not_secure_password',
            })
        self.assertEqual(response.status_code, 201)
        user: dict = response.json()
        self.assertTrue('id' in user)
        self.assertFalse('password' in user)
        self.assertEqual(user['first_name'], 'John')
        self.assertEqual(user['last_name'], 'Doe')
        self.assertEqual(user['email'], 'user@email.com')
        self.assertEqual(user['phone'], '123456789')

        db_user = User.objects.get(id=user['id'])
        self.assertFalse(db_user.is_staff)
        self.assertFalse(db_user.is_superuser)
        self.assertFalse(db_user.is_active)
        self.assertEqual(db_user.email, 'user@email.com')

    def test_register_user_with_invalid_password(self):
        response: Response = self.fast_api_client.post(
            url="/fast-api/users",
            json={
                'email': 'user@email.com',
                'first_name': 'John',
                'last_name': 'Doe',
                'phone': '123456789',
                'password': 'random_not_secure_password',
                'repeated_password': 'does not match',
            })
        self.assertEqual(response.status_code, 422)
        response: dict = response.json()
        self.assertEqual(response['status_code'], 422)
        self.assertEqual(len(response['errors']), 1)
        self.assertEqual(response['errors'][0]['message'], "Passwords don't match")
