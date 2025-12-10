from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Payout
from .tasks import payout_task


class PaymentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.payout_data = {
            "payment": "44",
            "currency": 643,
            "recip_details": "Hello",
            "status": 1,
            "description": "",
        }
        self.payout = Payout.objects.create(**self.payout_data)

    def test_get_payment(self):
        url = reverse("payouts_list_create")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1

    def test_create_payment(self):
        url = reverse("payouts_list_create")
        payout_data = {
            "payment": "55",
            "currency": 643,
            "recip_details": "World",
            "status": 1,
            "description": "",
        }
        response = self.client.post(url, payout_data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Payout.objects.count() == 2

    def test_invalid_create_payment(self):
        url = reverse("payouts_list_create")
        payout_data = {
            "payment": "55",
            "currency": 644,
            "recip_details": "World",
            "status": 5,
            "description": "",
        }
        response = self.client.post(url, payout_data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_patch_payment(self):
        url = reverse("payouts_detail", args=[self.payout.pk])
        response = self.client.get(url)
        payout_data = {
            "status": 2,
        }
        response = self.client.patch(url, payout_data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["status"] == 2

    def test_task(self):
        payout_task.run(self.payout.pk)
        p = Payout.objects.get(id=self.payout.pk)
        assert p.status == 2
