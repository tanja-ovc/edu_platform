from django.contrib import admin

from products.models import Lesson, LessonWatchData, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("name", "video_url", "length")


@admin.register(LessonWatchData)
class LessonWatchDataAdmin(admin.ModelAdmin):
    list_display = (
        "lesson",
        "product",
        "student",
        "time_watched",
        "last_watched",
    )
