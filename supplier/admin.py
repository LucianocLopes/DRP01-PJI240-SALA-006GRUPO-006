from django.contrib import admin

from .models import ContactSupplier, Supplier, PhoneContact, RequestSupplier, PhoneSupplier

# Register your models here.
# tabular
class ContactSupplierInline(admin.TabularInline):
    '''Tabular Inline View for models.ContactSupplier'''

    model = ContactSupplier
    min_num = 0
    max_num = 5
    extra = 1


class PhoneContactInline(admin.TabularInline):
    '''Tabular Inline View for PhoneContact'''

    model = PhoneContact
    min_num = 0
    max_num = 3
    extra = 0

class PhoneSupplierInline(admin.TabularInline):
    '''Tabular Inline View for PhoneSupplier'''

    model = PhoneSupplier
    min_num = 1
    max_num = 3
    extra = 0

class RequestSupplierInline(admin.TabularInline):
    '''Tabular Inline View for RequestSupplier'''

    model = RequestSupplier
    min_num = 0
    max_num = 999
    extra = 1


# admin
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    '''Admin View for Supplier'''

    list_display = ('company_name', 'fantasy_name', 'cnpj_number', 'is_active')
    list_filter = ('is_active',)
    inlines = [
        PhoneSupplierInline,
        ContactSupplierInline,
        RequestSupplierInline,
    ]


@admin.register(ContactSupplier)
class ContactSupplierAdmin(admin.ModelAdmin):
    '''Admin View for ContactSupplier'''

    list_display = ('first_name', 'last_name', 'e_mail')
    inlines = [
        PhoneContactInline,
    ]
