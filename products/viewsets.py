from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from products.filtersets import ProductFilterSet
from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related('category').prefetch_related('tags')
    serializer_class = ProductSerializer
    # GET, POST, PUT, PATCH, DELETE

    authentication_classes = []
    permission_classes = []
    filterset_class = ProductFilterSet
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'price', 'id']
