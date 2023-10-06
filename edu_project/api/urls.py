from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import MyLessonsWatchDataViewSet, ProductViewSet

router = DefaultRouter()


router.register("my-lessons", MyLessonsWatchDataViewSet, basename="my-lessons")
router.register("products", ProductViewSet, basename="products")

urlpatterns = [
    path("", include(router.urls)),
]
