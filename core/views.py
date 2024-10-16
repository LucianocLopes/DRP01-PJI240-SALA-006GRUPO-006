from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views import View
from suppli_request import models


class IndexView(ListView):
    login_required = True
    model = models.SupplyResquest
    template_name = "core/index.html"


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(TemplateView):
    template_name = 'registration/logout.html'
    
    def post(self, request):
        logout(request)
        return redirect('login')

