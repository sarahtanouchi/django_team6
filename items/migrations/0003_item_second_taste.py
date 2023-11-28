# Generated by Django 2.2.20 on 2023-11-28 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20231126_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='second_taste',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_taste', to='items.Taste', verbose_name='テイスト2'),
        ),
    ]