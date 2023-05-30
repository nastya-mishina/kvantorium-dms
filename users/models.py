from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    POSITIONS = (
        ('data', 'Дата-Квантум'),
        ('it', 'IT-Квантум'),
        ('robot', 'Робо-Квантум'),
        ('hightech', 'Хайтек'),
        ('geo', 'Гео-Квантум'),
        ('shah', 'Шахматы'),
        ('other', 'Другое'),
        ('kvant', 'Кванториум'),
    )
    middle_name = models.CharField(max_length=30, verbose_name="Отчество",
                                   default="")
    position = models.CharField(max_length=30, choices=POSITIONS,
                                verbose_name="Должность", default="")
    phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phoneRegex], max_length=12, unique=True,
                             verbose_name="Номер телефона (Через +7)")
    password = models.CharField(max_length=2000, verbose_name="Пароль",
                                default="pbkdf2_sha256$390000$jNQoFll3T4NGf109vDxvYX$wzXUUE3zThacoBzb0BE4x89F4N6qtUtpF1z2vYFpg/c=")
    PublicKey = models.FileField(verbose_name='Публичный ключ', blank=True)
    image = models.ImageField(verbose_name='Фото', upload_to='users/', blank=True)

    class Meta:
        verbose_name_plural = "Пользователи"
