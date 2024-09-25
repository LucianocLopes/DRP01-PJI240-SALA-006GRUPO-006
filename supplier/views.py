from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.http import HttpResponseRedirect
from .models import Supplier, PhoneSupplier, ContactSupplier, PhoneContact

from .forms import SupplierForm, PhoneSupplier

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
        context['phones'] = PhoneSupplier.objects.filter(supplier_id = self.object)
        context['contacts'] = ContactSupplier.objects.filter(supplier_id = self.object)
        context['phones_contact'] = PhoneContact.objects.all()
        return context


class DeleteView(TemplateView):
    template_name = "supplier/CRUD/supplier/delete.html"




# PHONE SUPPLIER

class PhoneSupplierCreateView(CreateView):
    model = PhoneSupplier
    template_name = "supplier/CRUD/phones_supplier/create.html"
    
    
    
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
        
        print(supplier)
        
        
        self.object.supplier_id = supplier
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())