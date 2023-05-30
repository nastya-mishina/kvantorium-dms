# Generated by Django 4.1.7 on 2023-05-19 07:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('document', '0002_document_signature'),
    ]

    operations = [
        migrations.CreateModel(
            name='SigDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_doc', models.FileField(upload_to='', verbose_name='Подписанный Файл')),
                ('doc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='document.document')),
                ('signatory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signatory', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
