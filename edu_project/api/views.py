from django.contrib.auth import get_user_model
from django.db.models import Sum, Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions, viewsets

from api.filters import ProductFilter
from api.serializers import (
    MyLessonsWatchDataSerializer,
    MyLessonsWatchDataPlusSerializer,
    ProductSerializer,
)
from products.models import LessonWatchData, Product

User = get_user_model()


class MyLessonsWatchDataViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        current_user = self.request.user
        return LessonWatchData.objects.filter(student=current_user).select_related(
            "lesson", "product"
        )

    def get_serializer_class(self):
        if self.request.query_params.get("product"):
            return MyLessonsWatchDataPlusSerializer
        return MyLessonsWatchDataSerializer


class ProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.prefetch_related(
        Prefetch(
            "watch_stats",
            queryset=LessonWatchData.objects.select_related("lesson"),
        ),
        Prefetch("owners"),
    ).annotate(
        time_watched_in_total=Sum("watch_stats__time_watched"),
    )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["all_users_count"] = User.objects.count()
        return context
