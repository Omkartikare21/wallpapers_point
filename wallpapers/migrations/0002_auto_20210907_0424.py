# Generated by Django 3.2.6 on 2021-09-07 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallpapers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='wallpapers',
            options={'verbose_name_plural': 'Wallpapers'},
        ),
    ]