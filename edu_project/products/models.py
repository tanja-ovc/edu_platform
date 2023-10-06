from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

User = get_user_model()


class Product(models.Model):
    name = models.CharField("название продукта", max_length=70, unique=True)
    owners = models.ManyToManyField(
        User,
        verbose_name="владельцы продукта",
        related_name="products_owned",
        blank=True,
    )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    def __str__(self):
        return f"{self.name}"


class Lesson(models.Model):
    name = models.CharField("название урока", max_length=120, unique=True)
    video_url = models.URLField("ссылка на видео урока", unique=True)
    length = models.PositiveSmallIntegerField("продолжительность урока (сек.)")
    associated_products = models.ManyToManyField(
        Product,
        verbose_name="находится в продуктах",
        related_name="lessons_included",
    )

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"

    def __str__(self):
        return f"{self.name}"


class LessonWatchData(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="урок",
        related_name="watch_stats",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="продукт",
        related_name="watch_stats",
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="студент",
        related_name="watch_stats",
    )
    time_watched = models.PositiveSmallIntegerField("просмотрено (сек.)", default=0)
    last_watched = models.DateField("дата последнего просмотра", blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "product", "lesson"],
                name="unique_lesson_in_product_for_student",
            )
        ]
        verbose_name = "данные о просмотре урока"
        verbose_name_plural = "данные о просмотрах уроков"

    def __str__(self):
        return f"Просмотр урока {self.lesson} студентом {self.student}"

    def clean(self):
        associated_lesson = Lesson.objects.filter(id=self.lesson.id).first()
        if self.time_watched > associated_lesson.length:
            raise ValidationError(
                "Время просмотра не может превышать продолжительность урока."
            )
