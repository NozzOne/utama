# Generated by Django 4.0.1 on 2022-01-17 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utama', '0009_remove_episode_title_remove_episode_titleen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
