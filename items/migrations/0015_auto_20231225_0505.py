# Generated by Django 2.2.20 on 2023-12-24 20:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0014_auto_20231216_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(default=0, verbose_name='評価'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, max_length=200, verbose_name='コメント'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('item', 'user')},
        ),
        migrations.RemoveField(
            model_name='review',
            name='rate',
        ),
    ]