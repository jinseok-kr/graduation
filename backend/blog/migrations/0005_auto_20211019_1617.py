# Generated by Django 3.2.5 on 2021-10-19 16:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_scrap'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='scrap',
            field=models.ManyToManyField(related_name='scrapping', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Scrap',
        ),
    ]
