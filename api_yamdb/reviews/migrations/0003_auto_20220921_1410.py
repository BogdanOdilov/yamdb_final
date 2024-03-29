# Generated by Django 2.2.16 on 2022-09-21 11:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220917_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, 'Допустимы значения от 1 до 10'), django.core.validators.MaxValueValidator(10, 'Допустимы значения от 1 до 10')], verbose_name='Рейтинг'),
        ),
    ]
