# Generated by Django 2.2.20 on 2023-11-26 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tea_set_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='茶器タイプ名')),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.Area', verbose_name='生産地'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.Item_type', verbose_name='商品タイプ'),
        ),
        migrations.AlterField(
            model_name='item',
            name='occasion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.Occasion', verbose_name='利用シーン'),
        ),
        migrations.AlterField(
            model_name='item',
            name='taste',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.Taste', verbose_name='テイスト'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tea_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.Tea_type', verbose_name='お茶タイプ'),
        ),
        migrations.AlterField(
            model_name='occasion',
            name='name',
            field=models.CharField(max_length=200, verbose_name='利用シーン名'),
        ),
        migrations.AlterField(
            model_name='tea_type',
            name='name',
            field=models.CharField(max_length=200, verbose_name='お茶タイプ名'),
        ),
        migrations.AddField(
            model_name='item',
            name='tea_set_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.Tea_set_type', verbose_name='茶器タイプ'),
        ),
    ]