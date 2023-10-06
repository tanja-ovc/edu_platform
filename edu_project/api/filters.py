from django_filters import rest_framework as filters

from products.models import LessonWatchData


class ProductFilter(filters.FilterSet):
    product = filters.NumberFilter(field_name="product", lookup_expr="id__exact")

    class Meta:
        model = LessonWatchData
        fields = ("product",)
