from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import IndexView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path("", login_required(IndexView.as_view()), name='index'),
    path("supplier/", include('supplier.urls')),
    path("suppli_request/", include('suppli_request.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
