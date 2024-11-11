from django.urls import path
from .views import ProductViewSet, WarehouseViewSet

urlpatterns = [
    path('products/', ProductViewSet.as_view({'get': 'list'})), 
    path('products/<str:code>/', ProductViewSet.as_view({'get': 'retrieve'})),  
    path('warehouses/', WarehouseViewSet.as_view({'get': 'list'})),  
    path('warehouses/<int:warehouse_id>/products/', WarehouseViewSet.as_view({'get': 'list'})),
]
