from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):
    template_name = "supplier/index.html"


class DeleteView(TemplateView):
    template_name = "supplier/CRUD/delete.html"