# Generated by Django 3.2.12 on 2023-05-29 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_secretkey'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/', verbose_name='Фото'),
        ),
    ]
