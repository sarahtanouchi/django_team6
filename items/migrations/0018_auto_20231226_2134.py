# Generated by Django 2.2.20 on 2023-12-26 12:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_auto_20231226_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='star',
            field=models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='評価'),
        ),
    ]
