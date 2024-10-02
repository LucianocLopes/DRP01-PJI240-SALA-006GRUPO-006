from django.urls import path, include

from supplier import views

urlpatterns = [
    path("", views.SupplierListView.as_view(), name="supplier-index"),
    path("Detail/<int:pk>/", views.SupplierDetailView.as_view(), name="supplier-detail"),
    path("new", views.SupplierCreateView.as_view(), name="supplier-new"),    
    # path("detail", IndexView.as_view(), name="supplier-index"),
    path("delete/", views.DeleteView.as_view(), name="supplier-delete"),
    # CRUD phone_supplier
    path("NewPhoneNumber/<int:int>/", views.PhoneSupplierCreateView.as_view(), name="supplier-createphone"),
    # CRUD contact_supplier
    path("NewContact/<int:int>/", views.ContactSupplierCreateView.as_view(), name="supplier-createcontact"),
    # CRUD phone contact_supplier
    path("NewPhoneContact/<int:int>/<int:int2>/", views.PhoneContactCreateView.as_view(), name="supplier-createphonecontact"),
]