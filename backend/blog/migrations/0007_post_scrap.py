# Generated by Django 3.2.5 on 2021-10-28 14:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_remove_post_scrap'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='scrap',
            field=models.ManyToManyField(blank=True, related_name='scrap_post', to=settings.AUTH_USER_MODEL),
        ),
    ]