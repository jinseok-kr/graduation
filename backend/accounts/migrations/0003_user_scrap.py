# Generated by Django 3.2.5 on 2021-10-24 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_scrap'),
        ('accounts', '0002_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='scrap',
            field=models.ManyToManyField(related_name='scrapnews', to='blog.Post'),
        ),
    ]
