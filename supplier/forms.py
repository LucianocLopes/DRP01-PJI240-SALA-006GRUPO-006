from django import forms
from django.forms.models import inlineformset_factory

from django.utils.translation import gettext as _

from .models import Supplier, PhoneSupplier

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, Row, Column


PhoneSupplierFormset = inlineformset_factory(Supplier, PhoneSupplier, fields=('type_phone', 'ddi_number', 'ddd_number', 'phone_number'), extra=3)


class SupplierForm(forms.ModelForm):
    
    class Meta:
        model = Supplier
        fields = '__all__'


class PhoneSupplierForm(forms.ModelForm):
    
    class Meta:
        model = PhoneSupplier
        fields = '__all__'