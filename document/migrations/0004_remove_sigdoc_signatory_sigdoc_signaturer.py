# Generated by Django 4.1.7 on 2023-05-19 08:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('document', '0003_sigdoc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sigdoc',
            name='signatory',
        ),
        migrations.AddField(
            model_name='sigdoc',
            name='signaturer',
            field=models.ForeignKey(blank=True, default=123, on_delete=django.db.models.deletion.CASCADE, related_name='signaturer', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
