# Generated by Django 2.2.20 on 2024-01-06 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20231231_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.Coupon'),
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]