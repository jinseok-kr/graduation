# Generated by Django 3.2.5 on 2021-11-04 13:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20211104_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='scrap',
            field=models.ManyToManyField(blank=True, related_name='scrap_news', to=settings.AUTH_USER_MODEL),
        ),
    ]