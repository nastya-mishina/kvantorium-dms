# Generated by Django 4.1.7 on 2023-05-19 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_remove_sigdoc_signatory_sigdoc_signaturer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sigdoc',
            options={'verbose_name_plural': 'Подписанные Документы'},
        ),
    ]