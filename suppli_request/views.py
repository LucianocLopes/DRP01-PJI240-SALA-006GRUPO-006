from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.http import HttpResponseRedirect

from suppli_request import models

# Create your views here.

# MIXINS
# VIEWS

class SupplyResquestListView(ListView):
    model = models.SupplyResquest
    template_name = "suppli_request/index.html"


class SupplyRequestCreateView(CreateView):
    model = models.SupplyResquest
    template_name = "suppli_request/supplyrequest/CRUD/create.html"
    fields = ["date_request", "description_request", "status"]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class SupplyRequestDetailView(DetailView):
    model = models.SupplyResquest
    template_name = "suppli_request/supplyrequest/CRUD/detail.html"


# Views para Contato e Sobre
def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')