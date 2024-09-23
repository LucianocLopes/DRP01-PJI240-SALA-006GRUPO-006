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
        
    # def __init__(self, *args, **kwargs):
    #     super(SupplierForm, self).__init__(*args, **kwargs)
        
    #     self.helper = FormHelper(self)
    #     self.helper.layout = Layout(
    #     Row(
    #         Column('is_active', css_class='col-md-2'),
    #         Column('company_name', css_class='col-md-8'),
    #     ),
    #     Row(
    #         Column('fantasy_name', css_class='col-md-7'),
    #         Column('cnpj_number', css_class='col-md-5'),
    #     ),
    #     Row(
    #         Column('e_mail', css_class='col-md-12'),
    #     ),
    #     )