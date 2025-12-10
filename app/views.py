from typing import Any

from rest_framework import generics, mixins
from rest_framework.serializers import BaseSerializer

from .models import Payout
from .serializers import PayoutSerializer, PayoutPatchSerializer
from .tasks import payout_task


class PayoutList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Payout.objects.all()
    serializer_class = PayoutSerializer

    def get(self, request: Any, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Any, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer: BaseSerializer):
        serializer.save()
        payout_task.delay(serializer.data["id"])


class PayoutDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Payout.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return PayoutPatchSerializer
        return PayoutSerializer

    def get(self, request: Any, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request: Any, *args, **kwargs):        
        return self.update(request, *args, **kwargs)

    def delete(self, request: Any, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
