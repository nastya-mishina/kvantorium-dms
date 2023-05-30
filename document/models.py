from django.db import models

from users.forms import User


class Document(models.Model):
    file = models.FileField(verbose_name='Файл')
    name = models.CharField(max_length=100, verbose_name='Название документа', default="")
    signature = models.ManyToManyField(User, blank=True, related_name='user')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='document'
    )

    class Meta:
        verbose_name_plural = "Документы"


class SigDoc(models.Model):
    sign_doc = models.FileField(verbose_name='Подписанный Файл')
    doc = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='document')
    signaturer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='signaturer', blank=True
    )

    class Meta:
        verbose_name_plural = "Подписанные Документы"


class Event(models.Model):
    date = models.CharField(max_length=255, verbose_name='Дата')
    time = models.CharField(max_length=255, verbose_name='Время')
    short_text = models.CharField(max_length=100, verbose_name='Описание', default=" ")
    text = models.CharField(max_length=3500, verbose_name='Текст', default="")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='events'
    )

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = "Мероприятия"


class Report(models.Model):
    file = models.FileField(verbose_name='Файл')
    name = models.CharField(max_length=100, verbose_name='Название отчёта', default="")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='report'
    )

    class Meta:
        verbose_name_plural = "Отчёты"
