# Generated by Django 2.2.20 on 2023-12-27 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0018_auto_20231226_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='タイトル')),
                ('body', models.TextField(max_length=50, verbose_name='本文')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
            ],
        ),
        migrations.RenameField(
            model_name='review',
            old_name='star',
            new_name='rate',
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('item', 'user')},
            },
        ),
    ]
