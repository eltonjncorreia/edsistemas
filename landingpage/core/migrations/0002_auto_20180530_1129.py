# Generated by Django 2.0.5 on 2018-05-30 14:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^(\\d+)$')], verbose_name='Telefone'),
        ),
    ]