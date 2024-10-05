from django.urls import path, include

from suppli_request import views

urlpatterns = [
    path("", views.SupplyRequestView.as_view(), name="suppli_request-index"),
]