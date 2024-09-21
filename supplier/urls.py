from django.urls import path, include

from .views import IndexView, DeleteView

urlpatterns = [
    path("", IndexView.as_view(), name="supplier-index"),
    path("delete/", DeleteView.as_view(), name="supplier-delete"),
]