from django.db import models


class Course(models.Model):
    title = models.CharField(
        max_length=240,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    preview = models.ImageField(
        upload_to="course/preview",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="описание курса",
        help_text="Введите описание курса",
    )
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Владелец', help_text='Укажите владельца курса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["title"]


class Lesson(models.Model):
    title = models.CharField(
        max_length=240,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    preview_lesson = models.ImageField(
        upload_to="course/preview_lesson",
        blank=True,
        null=True,
        verbose_name="Превью урока",
        help_text="Загрузите превью урока",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="описание урока",
        help_text="Введите описание урока",
    )
    reference = models.ForeignKey(
        Course,
        verbose_name="Курс",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="Lessons",
    )
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Владелец',
                              help_text='Укажите владельца')

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["title"]

    def __str__(self):
        return self.title
