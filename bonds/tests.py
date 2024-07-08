from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Bond


class BondTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='qwerty')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        Bond.objects.create(user=self.user, name='Test Bond', isin='CZ0003551252', value=1000, interest_rate=5,
                            purchase_date='2024-01-01', maturity_date='2025-01-01', interest_payment_frequency='annual')

    def test_bond_creation(self):
        bond = Bond.objects.get(name='Test Bond')
        self.assertEqual(bond.value, 1000)

    def test_get_bonds(self):
        url = '/api/bonds/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Bond')

    def test_create_bond_with_valid_isin(self):
        url = '/api/bonds/'
        data = {
            'name': 'Another Test Bond',
            'isin': 'CZ0003551251',
            'value': 2000,
            'interest_rate': 4,
            'purchase_date': '2023-01-01',
            'maturity_date': '2026-01-01',
            'interest_payment_frequency': 'annual',
            'user': self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bond.objects.count(), 2)
        bond = Bond.objects.get(name='Another Test Bond')
        self.assertEqual(bond.value, 2000)

    def test_delete_bond(self):
        bond = Bond.objects.get(name='Test Bond')
        url = f'/api/bonds/{bond.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Bond.objects.count(), 0)