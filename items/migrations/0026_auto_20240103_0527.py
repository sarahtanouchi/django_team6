# Generated by Django 2.2.20 on 2024-01-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0025_auto_20240102_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='recommended',
            field=models.BooleanField(default=None, null=True, verbose_name='おすすめ'),
        ),
    ]
