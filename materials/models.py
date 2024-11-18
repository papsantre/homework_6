from django.conf import settings
from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    """
    Класс для описания модели курсов
    """

    title = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    description = models.TextField(
        verbose_name="Описание курса", **NULLABLE, help_text="Введите описание курса"
    )
    image = models.ImageField(
        upload_to="materials/course",
        verbose_name="Превью",
        **NULLABLE,
        help_text="Загрузите превью",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE
    )


class Lesson(models.Model):
    """
    Класс для описания модели уроков
    """

    title = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        verbose_name="Описание урока", **NULLABLE, help_text="Введите описание урока"
    )
    image = models.ImageField(
        upload_to="materials/lesson",
        verbose_name="Превью",
        **NULLABLE,
        help_text="Загрузите превью",
    )
    video_link = models.URLField(
        **NULLABLE, verbose_name="Ссылка на видео", help_text="Укажите ссылку на видео"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        related_name="lesson_count",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Пользователь",
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, **NULLABLE, verbose_name="Курс", related_name="subscription_course"
    )
    sign_up = models.BooleanField(default=False, verbose_name="Подписка")

    def __str__(self):
        return f"{self.user}: ({self.course})"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
