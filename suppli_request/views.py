from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


from suppli_request import models

# Create your views here.

# MIXINS
# VIEWS

class SupplyResquestListView(LoginRequiredMixin, ListView):
    model = models.SupplyResquest
    template_name = "suppli_request/index.html"
    paginate_by = 10


class SupplyRequestCreateView(LoginRequiredMixin,CreateView):
    model = models.SupplyResquest
    template_name = "suppli_request/supplyrequest/CRUD/create.html"
    fields = ["date_request", "description_request", "status"]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class SupplyItensRequestCreateView(LoginRequiredMixin, CreateView):
    model = models.ItensSupplyRequest
    template_name = "suppli_request/supplyrequest/CRUD/itens/create.html"
    fields = ['code_item_request',
                'description_item',
                'amount_item',
                'unit_measurement',
                'unit_value',
            ]
    def get_context_data(self, **kwargs):
        context = super(SupplyItensRequestCreateView, self).get_context_data(**kwargs)
        
        pk_int = self.kwargs['int']
        context['pk_int'] = pk_int
        
        return context    
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        supply_request = models.SupplyResquest.objects.get(id=self.kwargs['int'])
        
        self.object.supply_request = supply_request
        print(self.object)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class SupplyRequestDetailView(LoginRequiredMixin, DetailView):
    model = models.SupplyResquest
    template_name = "suppli_request/supplyrequest/CRUD/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(SupplyRequestDetailView, self).get_context_data(**kwargs)
        
        itens = models.ItensSupplyRequest.objects.filter(supply_request=self.object)
        
        context['itens'] = itens
        
        return context


class SupplyRequestUpdateView(LoginRequiredMixin, UpdateView):
    model = models.SupplyResquest
    template_name = "suppli_request/supplyrequest/CRUD/update.html"    
    fields = ["date_request",
                "description_request",
                "status",
            ]

    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to    

class SupplyRequestSupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = models.SupplyResquest
    template_name = "suppli_request/supplyrequest/CRUD/update_supplier.html"    
    fields = ["supplier",
                "start_date",
                'delivery_time',
            ]
    
    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to    

class SupplyItensRequestUpdateView(LoginRequiredMixin, UpdateView):
    model = models.ItensSupplyRequest
    template_name = "suppli_request/supplyrequest/CRUD/itens/update.html"    
    fields = ['code_item_request',
                'description_item',
                'amount_item',
                'unit_measurement',
                'unit_value',
            ]
    
    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to


class SupplyRequestDeleteView(LoginRequiredMixin, DeleteView):
    model = models.SupplyResquest
    template_name = "suppli_request/supplyrequest/CRUD/delete.html"    
    
    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to

class SupplyItensRequestDeleteView(LoginRequiredMixin, DeleteView):
    model = models.ItensSupplyRequest
    template_name = "suppli_request/supplyrequest/CRUD/itens/delete.html"
    
    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to


# Views para Contato e Sobre
def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')