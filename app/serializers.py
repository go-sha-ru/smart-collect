from rest_framework import serializers

from .models import Payout


class PayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payout
        fields = [
            "id",
            "payment",
            "currency",
            "recip_details",
            "status",
            "description",
            "created_at",
            "updated_at",
        ]


class PayoutPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payout
        fields = [
            "status",
        ]
