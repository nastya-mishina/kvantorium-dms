# Generated by Django 4.1.7 on 2023-05-19 07:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='signature',
            field=models.ManyToManyField(blank=True, related_name='signature', to=settings.AUTH_USER_MODEL),
        ),
    ]
