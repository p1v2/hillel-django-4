from django_filters import FilterSet, CharFilter, BooleanFilter

from products.models import Product


class ProductFilterSet(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    price__gte = CharFilter(field_name='price', lookup_expr='gte')
    price__lte = CharFilter(field_name='price', lookup_expr='lte')

    # cheap=1 returns products with price less than 20
    cheap = CharFilter(method='filter_cheap')

    def filter_cheap(self, queryset, name, value):
        if value:
            # lt - less than
            # lte - less than or equal
            return queryset.filter(price__lt=20)
        return queryset

    category = CharFilter(field_name='category__name', lookup_expr='icontains')
    tag = CharFilter(field_name='tags__name', lookup_expr='icontains')
    tags = CharFilter(method='filter_tags')

    def filter_tags(self, queryset, name, value):
        tags = value.split(',')

        for tag in tags:
            queryset = queryset.filter(tags__name__icontains=tag)

        return queryset

    # q = CharFilter(method='filter_q', label='Query')
    #
    # def filter_q(self, queryset, name, value):
    #     return (queryset.filter(name__icontains=value) |
    #             queryset.filter(tags__name__icontains=value) |
    #             queryset.filter(category__name__icontains=value) |
    #             queryset.filter(description__icontains=value))

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'tag', 'is_18_plus']
