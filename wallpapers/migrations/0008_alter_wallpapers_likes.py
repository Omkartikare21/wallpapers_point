# Generated by Django 3.2.6 on 2021-10-03 12:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallpapers', '0007_wallpapers_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallpapers',
            name='likes',
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]