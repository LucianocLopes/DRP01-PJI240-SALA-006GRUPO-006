from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

# Create your views here.

# MIXINS
# VIEWS

class SupplyRequestView(TemplateView):
    template_name = "suppli_request/index.html"
