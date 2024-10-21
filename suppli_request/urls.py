from django.urls import path, include
from suppli_request import views

urlpatterns = [
    path("", views.SupplyResquestListView.as_view(), name="suppli_request-index"),
    # CRUD
    path("NewRequest/", views.SupplyRequestCreateView.as_view(), name="suppli_request-new"),
    path("UpdateRequest/<int:pk>/", views.SupplyRequestUpdateView.as_view(), name="suppli_request-update"),
    path("Detail/<int:pk>/", views.SupplyRequestDetailView.as_view(), name="suppli_request-detail"),
    path("AddSupplierRequest/<int:pk>/", views.SupplyRequestSupplierUpdateView.as_view(), name="suppli_request-update-supplier"),
    path("AddItensRequest/<int:int>/", views.SupplyItensRequestCreateView.as_view(), name="suppli_request-additens_request")
]