# Generated by Django 4.0.1 on 2022-01-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utama', '0011_alter_anime_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=models.ManyToManyField(through='utama.AnimeGenres', to='utama.Genres'),
        ),
    ]
