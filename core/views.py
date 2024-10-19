from django.db.models import Avg, F, Window, Sum, Count, Q, ExpressionWrapper, FloatField
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views import View

from suppli_request import models
from supplier import models as suppliermodels

class IndexView(ListView):
    login_required = True
    model = models.SupplyResquest
    template_name = "core/index.html"
    paginate_by = 3
    
    def get_queryset(self):
        query = models.SupplyResquest.objects.all().order_by('-created')
    
        return query

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        supplyers = suppliermodels.Supplier.objects.annotate(
            total=Count('id')
        )
        
        actives = suppliermodels.Supplier.objects.filter(is_active=True)
        
        complet = models.SupplyResquest.objects.filter(
            Q(status='CP') 
        ).annotate(
            valuetotal=ExpressionWrapper(
                F('itenssupplyrequest__unit_value') * F('itenssupplyrequest__amount_item'), 
                output_field=FloatField())
        )
        completed = complet.aggregate(
            soma=Sum('valuetotal')
        )
        
        prog = models.SupplyResquest.objects.filter(
            Q(status='IP')
        ).annotate(
            valuetotal=ExpressionWrapper(
                F('itenssupplyrequest__unit_value') * F('itenssupplyrequest__amount_item'), 
                output_field=FloatField())
        )
        progress = prog.aggregate(
            soma=Sum('valuetotal')
        )
        
        open = models.SupplyResquest.objects.filter(
            Q(status='ST') | Q(status='IP')
        ).annotate(
            valuetotal=ExpressionWrapper(
                F('itenssupplyrequest__unit_value') * F('itenssupplyrequest__amount_item'), 
                output_field=FloatField())
        )
        opening = open.aggregate(
            soma=Sum('valuetotal')
        )
        
        alln = models.SupplyResquest.objects.filter(
            Q(status='CP') | Q(status='ST') | Q(status='IP')
        ).annotate(
            valuetotal=ExpressionWrapper(
                F('itenssupplyrequest__unit_value') * F('itenssupplyrequest__amount_item'), 
                output_field=FloatField())
        )
        allnumber = alln.aggregate(
            soma=Sum('valuetotal')
        )
        
        
        context['supplyers'] = supplyers
        context['actives'] = actives
        context['completed'] = completed
        context['progress'] = progress
        context['opening'] = opening
        context['allnumber'] = allnumber
        
        return context


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(TemplateView):
    template_name = 'registration/logout.html'
    
    def post(self, request):
        logout(request)
        return redirect('login')

