# Generated by Django 4.1.7 on 2023-05-19 07:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='Файл')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Название отчёта')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Отчёты',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255, verbose_name='Дата')),
                ('time', models.CharField(max_length=255, verbose_name='Время')),
                ('short_text', models.CharField(default=' ', max_length=100, verbose_name='Описание')),
                ('text', models.CharField(default='', max_length=3500, verbose_name='Текст')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='Файл')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Название документа')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Документы',
            },
        ),
    ]
