from django.urls import path

from app import views

urlpatterns = [
    path("payouts/", views.PayoutList.as_view(), name="payouts_list_create"),
    path("payouts/<int:pk>/", views.PayoutDetail.as_view(), name="payouts_detail"),
]
