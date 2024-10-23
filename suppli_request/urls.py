from django.urls import path, include
from suppli_request import views

urlpatterns = [
    path("", views.SupplyResquestListView.as_view(), name="suppli_request-index"),
    # CRUD
    path("NewRequest/", views.SupplyRequestCreateView.as_view(), name="suppli_request-new"),
    path("UpdateRequest/<int:pk>/", views.SupplyRequestUpdateView.as_view(), name="suppli_request-update"),
    path("DeleteRequest/<int:pk>/", views.SupplyRequestDeleteView.as_view(), name="suppli_request-delete"),
    path("Detail/<int:pk>/", views.SupplyRequestDetailView.as_view(), name="suppli_request-detail"),
    path("AddSupplierRequest/<int:pk>/", views.SupplyRequestSupplierUpdateView.as_view(), name="suppli_request-update-supplier"),
    path("AddItensRequest/<int:int>/", views.SupplyItensRequestCreateView.as_view(), name="suppli_request-additens_request"),
    path("UpdateItemRequest/<int:pk>/", views.SupplyItensRequestUpdateView.as_view(), name="suppli_request-updateitem_request"),
    path("DeleteItemRequest/<int:pk>/", views.SupplyItensRequestDeleteView.as_view(), name="suppli_request-deleteitem_request"),
]