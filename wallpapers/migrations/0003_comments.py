# Generated by Django 3.2.6 on 2021-09-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpapers', '0002_auto_20210907_0424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=80)),
                ('user_email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
    ]