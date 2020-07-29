from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from wallets.models import Wallet


class TransactionTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='test_user', password='test')
        res = self.client.post('/login/', {'username': user.username, 'password': 'test'})
        self.token = res.data['token']
        self.wallet_1 = Wallet.objects.create(owner=user)
        self.wallet_2 = Wallet.objects.create(owner=user)

    def test_create_transaction_unauthorized(self):
        response = self.client.post('/transactions/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_transaction_no_data(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post('/transactions/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_transaction(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        data = {
            'from_wallet': self.wallet_1.address,
            'to_wallet': self.wallet_2.address,
            'amount': 0.1,
        }
        response = self.client.post('/transactions/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
