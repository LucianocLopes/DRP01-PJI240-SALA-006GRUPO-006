from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views import View

class IndexView(TemplateView):
    login_required = True
    template_name = "core/index.html"

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(TemplateView):
    template_name = 'registration/logout.html'
    
    def post(self, request):
        logout(request)
        return redirect('login')

