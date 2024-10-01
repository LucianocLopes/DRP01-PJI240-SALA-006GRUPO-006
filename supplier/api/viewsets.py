from rest_framework import viewsets
from supplier.api import serializers

from supplier import models


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SupplierSerializer
    queryset = models.Supplier.objects.all()