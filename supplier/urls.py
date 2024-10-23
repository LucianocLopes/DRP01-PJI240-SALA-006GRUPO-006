from django.urls import path, include

from supplier import views as v

urlpatterns = [
    path("", v.SupplierListView.as_view(), name="supplier-index"),
    path("Detail/<int:pk>/", v.SupplierDetailView.as_view(), name="supplier-detail"),
    path("Update/<int:pk>/", v.SupplierUpdateView.as_view(), name="supplier-update"),
    path("new", v.SupplierCreateView.as_view(), name="supplier-new"),    
    # path("detail", IndexView.as_view(), name="supplier-index"),
    path("ConfirmDelete/<int:pk>/",  v.SupplierDeleteView.as_view(), name="supplier-delete"),
    # CRUD phone_supplier
    path("NewPhoneNumber/<int:int>/", v.PhoneSupplierCreateView.as_view(), name="supplier-createphone"),
    path("UpdatePhoneNumber/<int:pk>/", v.PhoneSupplierUpdateView.as_view(), name="supplier-updatephone"),
    path("Phone/ConfirmDelete/<int:pk>/",  v.PhoneSupplierDeleteView.as_view(), name="supplier-deletephone"),
    # CRUD contact_supplier
    path("NewContact/<int:int>/", v.ContactSupplierCreateView.as_view(), name="supplier-createcontact"),
    path("UpdateContact/<int:pk>/", v.ContactSupplierUpdateView.as_view(), name="supplier-updatecontact"),
    path("Contact/ConfirmDelete/<int:pk>/",  v.ContactSupplierDeleteView.as_view(), name="supplier-deletecontact"),
    # CRUD phone contact_supplier
    path("NewPhoneContact/<int:int>/<int:int2>/", v.PhoneContactCreateView.as_view(), name="supplier-createphonecontact"),
    path("UpdatePhoneContact/<int:pk>/", v.PhoneContactUpdateView.as_view(), name="supplier-updatephonecontact"),
    path("PhoneContact/ConfirmDelete/<int:pk>/",  v.PhoneContactDeleteView.as_view(), name="supplier-deletephonecontact"),
]