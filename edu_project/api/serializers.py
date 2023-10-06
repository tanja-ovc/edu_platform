from rest_framework import serializers

from api.utils import lesson_is_fully_watched
from products.models import LessonWatchData, Product


class MyLessonsWatchDataSerializer(serializers.ModelSerializer):
    lesson = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    is_fully_watched = serializers.SerializerMethodField()

    class Meta:
        model = LessonWatchData
        fields = (
            "id",
            "lesson",
            "product",
            "time_watched",
            "is_fully_watched",
        )

    def get_is_fully_watched(self, obj):
        return lesson_is_fully_watched(obj)


class MyLessonsWatchDataPlusSerializer(MyLessonsWatchDataSerializer):
    class Meta:
        model = LessonWatchData
        fields = (
            "id",
            "lesson",
            "product",
            "time_watched",
            "last_watched",  # one field added in this serializer
            "is_fully_watched",
        )


class ProductSerializer(serializers.ModelSerializer):
    fully_watched_lessons_amount = serializers.SerializerMethodField()
    time_watched_in_total = serializers.IntegerField()
    owners_amount = serializers.SerializerMethodField()
    purchase_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "fully_watched_lessons_amount",
            "time_watched_in_total",
            "owners_amount",
            "purchase_percentage",
        )

    def get_owners_amount(self, obj):
        return obj.owners.count()

    def get_purchase_percentage(self, obj):
        users_sum_amount = self.context.get("all_users_count")
        return round(((obj.owners.count() / users_sum_amount) * 100), 2)

    def get_fully_watched_lessons_amount(self, obj):
        all_lesson_data = obj.watch_stats.all()
        amount = 0
        for lesson_data_set in all_lesson_data:
            if lesson_is_fully_watched(lesson_data_set):
                amount += 1
        return amount
