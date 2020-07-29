from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from wallets.models import Wallet


class WalletTest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='test_user', password='test')
        res = self.client.post('/login/', {'username': user.username, 'password': 'test'})
        self.token = res.data['token']

    def test_create_wallet(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post('/wallets/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, Wallet.objects.count())
