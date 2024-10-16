from django.urls import path, include

from suppli_request import views

urlpatterns = [
    path("", views.SupplyResquestListView.as_view(), name="suppli_request-index"),
    # CRUD
    path("New/", views.SupplyRequestCreateView.as_view(), name="suppli_request-new"),
    path("Detail/<int:pk>/", views.SupplyRequestDetailView.as_view(), name="suppli_request-detail"),
]