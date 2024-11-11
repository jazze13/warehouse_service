from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, Warehouse
from .serializers import ProductSerializer, WarehouseSerializer

# Create your views here.

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        warehouse_id = self.request.query_params.get('warehouse_id')
        if warehouse_id is not None:
            queryset = queryset.filter(warehouse_id=warehouse_id)

        code = self.request.query_params.get('code')
        if code is not None:
            queryset = queryset.filter(code=code)

        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category=category)

        return queryset



class WarehouseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer