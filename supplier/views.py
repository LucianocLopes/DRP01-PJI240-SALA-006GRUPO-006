from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.http import HttpResponseRedirect, request

from .models import Supplier, PhoneSupplier, ContactSupplier, PhoneContact
from suppli_request import models


from supplier.forms import SupplierForm, PhoneSupplier

# Create your views here.

# MIXINS
class SupplierFormValidMixin():
    def form_valid(self, form):
        context = self.get_context_data()
        phone_supplier_formset = context['phone_supplier_formset']
        
        self.obj = form.save()
        if phone_supplier_formset.is_valid():
            phone_supplier_formset.instance = self.obj
            phone_supplier_formset.save()
        return redirect('supplier-index')


class SupplierFieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ["is_active",
                    "company_name",
                    "fantasy_name",
                    "cnpj_number",
                    "e_mail",
                    ]
        return super().dispatch(request, *args, **kwargs)


#VIEWS
class SupplierListView(ListView):
    model = Supplier
    template_name = "supplier/index.html"
    context_object_name = 'supplier_list'
    paginate_by = 3


class SupplierCreateView(SupplierFieldsMixin, CreateView):
    model = Supplier
    template_name = "supplier/CRUD/supplier/create.html"
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "supplier/CRUD/supplier/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(SupplierDetailView, self).get_context_data(**kwargs)
        
        phones = PhoneSupplier.objects.filter(supplier_id = self.object)
        contacts = ContactSupplier.objects.filter(supplier_id = self.object)
        phones_contacts = PhoneContact.objects.filter(contact = contacts.first())
        supplyrequest = models.SupplyResquest.objects.filter(
            supplier=self.object
        )
        
        context['phones'] = phones
        context['contacts'] = contacts
        context['phones_contact'] = phones_contacts
        context['supplyrequest'] = supplyrequest
        
        return context


class DeleteView(TemplateView):
    template_name = "supplier/CRUD/supplier/delete.html"




# PHONE SUPPLIER

class PhoneSupplierCreateView(CreateView):
    model = PhoneSupplier
    template_name = "supplier/CRUD/phones_supplier/create.html"
    
    def get_context_data(self, **kwargs):
        context = super(PhoneSupplierCreateView, self).get_context_data(**kwargs)
        
        pk_int = self.kwargs['int']
        context['pk_int'] = pk_int
        return context    
    
    
    
    def dispatch(self, request, *args, **kwargs):
        self.fields = ["type_phone",
                    "ddi_number",
                    "ddd_number",
                    "phone_number",
                    ]
        return super().dispatch(request, *args, **kwargs)
    
    
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        supplier = Supplier.objects.get(id=self.kwargs['int'])
        
        self.object.supplier_id = supplier
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ContactSupplierCreateView(CreateView):
    model = ContactSupplier
    template_name = "supplier/CRUD/contact_supplier/create.html"
    
    def dispatch(self, request, *args, **kwargs):
        self.fields = ["first_name",
                    "last_name",
                    "position_company",
                    "e_mail",
                    "remarks",
                    ]
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ContactSupplierCreateView, self).get_context_data(**kwargs)
        
        pk_int = self.kwargs['int']
        context['pk_int'] = pk_int
        return context    
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        supplier = Supplier.objects.get(id=self.kwargs['int'])
        
        self.object.supplier_id = supplier
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class PhoneContactCreateView(CreateView):
    model = PhoneContact
    template_name = "supplier/CRUD/contact_supplier/phones_contact/create.html"
    
    
    fields = ["type_phone",
                "ddi_number",
                "ddd_number",
                "phone_number",
            ]
    def get_success_url(self):
        
        return reverse("supplier-detail", kwargs={"pk": self.kwargs['int']})

    
    def get_context_data(self, **kwargs):
        context = super(PhoneContactCreateView, self).get_context_data(**kwargs)
        
        pk_int = self.kwargs['int']
        context['pk_int'] = pk_int
        return context    
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        contact = ContactSupplier.objects.get(id=self.kwargs['int2'])
        
        self.object.contact = contact
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())
    


def search_cep(request):
    api = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/24/municipios"
    requisicao = requests.get(api)

    try:
        lista = requisicao.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "municipios": dicionario
    }

    return render(request, "index.html", contexto)