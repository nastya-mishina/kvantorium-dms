# Generated by Django 4.1.1 on 2023-04-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$jNQoFll3T4NGf109vDxvYX$wzXUUE3zThacoBzb0BE4x89F4N6qtUtpF1z2vYFpg/c=', max_length=2000, verbose_name='Пароль'),
        ),
    ]
