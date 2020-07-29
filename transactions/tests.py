from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class TransactionTests(APITestCase):
    def setUp(self):
        user = User.objects.create(username='test_user')
        user.set_password('test')
        user.save()
        res = self.client.post('/login/', {'username': user.username, 'password': 'test'})
        print(res)

    def test_create_transaction_unauthorized(self):
        response = self.client.post('/transactions/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
