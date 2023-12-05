# Generated by Django 2.2.20 on 2023-12-05 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20231202_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='area_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='生産地画像'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_images',
            field=models.ManyToManyField(blank=True, related_name='item', to='items.Image', verbose_name='商品画像'),
        ),
    ]
