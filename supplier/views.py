from django.shortcuts import redirect, render
from django.db.models import Avg, F, Window, Sum, Count, Q, ExpressionWrapper, FloatField
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect, request
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Supplier, PhoneSupplier, ContactSupplier, PhoneContact, AddressSupplier
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
class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = "supplier/index.html"
    context_object_name = 'supplier_list'
    paginate_by = 10

class SupplierCreateView(LoginRequiredMixin, SupplierFieldsMixin, CreateView):
    model = Supplier
    template_name = "supplier/CRUD/supplier/create.html"
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class SupplierDetailView(LoginRequiredMixin, DetailView):
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
        address = AddressSupplier.objects.filter(supplier = self.object).first()
        
        context['phones'] = phones
        context['contacts'] = contacts
        context['phones_contact'] = phones_contacts
        context['supplyrequest'] = supplyrequest
        context['address'] = address
        
        return context

# PHONE SUPPLIER
class PhoneSupplierCreateView(LoginRequiredMixin,CreateView):
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


class ContactSupplierCreateView(LoginRequiredMixin, CreateView):
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


class PhoneContactCreateView(LoginRequiredMixin, CreateView):
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


class SupplierUpdateView(LoginRequiredMixin, SupplierFieldsMixin, UpdateView):
    model = Supplier
    template_name = "supplier/CRUD/supplier/update.html"
    

class PhoneContactUpdateView(LoginRequiredMixin, UpdateView):
    model = PhoneContact
    template_name = "supplier/CRUD/contact_supplier/phones_contact/update.html"    
    fields = ["type_phone",
                "ddi_number",
                "ddd_number",
                "phone_number",
            ]
    
class ContactSupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = ContactSupplier
    fields = ["first_name",
                    "last_name",
                    "position_company",
                    "e_mail",
                    "remarks",
                ]
    template_name = "supplier/CRUD/contact_supplier/update.html"
    
class PhoneSupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = PhoneSupplier
    template_name = "supplier/CRUD/phones_supplier/update.html"
    fields = ["type_phone",
                "ddi_number",
                "ddd_number",
                "phone_number",
            ]


class PhoneContactDeleteView(DeleteView):
    model = PhoneContact
    template_name = "supplier/CRUD/contact_supplier/phones_contact/delete.html" 

    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to

class PhoneSupplierDeleteView(DeleteView):
    model = PhoneSupplier
    template_name = "supplier/CRUD/phones_supplier/delete.html" 

    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to

class ContactSupplierDeleteView(DeleteView):
    model = ContactSupplier
    template_name = "supplier/CRUD/contact_supplier/delete.html"
    

    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to



class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "supplier/CRUD/supplier/delete.html" 

    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to


# ADDRESS
class AddressSupplierCreateView(LoginRequiredMixin, CreateView):
    model = AddressSupplier
    template_name = "supplier/CRUD/address_supplier/create.html"
    
    def dispatch(self, request, *args, **kwargs):
        self.fields = ["address_type",
                        "zip_code",
                        "address",
                        "number",
                        "complement",
                        "district",
                        "city",
                        "state",
                        "ibge_code",
                        "gia_code",
                        "ddd_code",
                        "siafi_code",
                    ]
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(AddressSupplierCreateView, self).get_context_data(**kwargs)
        
        pk_int = self.kwargs['int']
        context['pk_int'] = pk_int
        return context
    
    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to    
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        supplier = Supplier.objects.get(id=self.kwargs['int'])
        
        self.object.supplier = supplier
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AddressSupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = AddressSupplier
    template_name = "supplier/CRUD/address_supplier/update.html"
    fields = ["address_type",
                        "zip_code",
                        "address",
                        "number",
                        "complement",
                        "district",
                        "city",
                        "state",
                        "ibge_code",
                        "gia_code",
                        "ddd_code",
                        "siafi_code",
                    ]

    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to 

class AddressSupplierDeleteView(DeleteView):
    model = AddressSupplier
    template_name = "supplier/CRUD/address_supplier/delete.html" 

    def get_success_url(self):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', '/'))
        return redirect_to