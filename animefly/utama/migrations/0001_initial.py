# Generated by Django 4.0.1 on 2022-01-09 08:20

import animefly.utama.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('titleEn', models.CharField(max_length=100)),
                ('titleEs', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tipo', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('release', models.DateField()),
                ('rating', models.CharField(max_length=50)),
                ('coverFilename', models.UUIDField(default='ef5dbb84c57642c68d116852ef175320', editable=False, unique=True)),
                ('cover', models.ImageField(upload_to=animefly.utama.models.UploadToPathAndRename('media/cover'))),
                ('backgroundFilename', models.UUIDField(default='001d915e97fa4a63bcd151a38bdc056c', editable=False, unique=True)),
                ('background', models.ImageField(upload_to=animefly.utama.models.UploadToPathAndRename('media/background'))),
                ('renderFilename', models.UUIDField(default='bc21eb1aa2514eeca207e1c67150c846', editable=False, unique=True)),
                ('render', models.ImageField(upload_to=animefly.utama.models.UploadToPathAndRename('media/render'))),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('episode', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('titleEn', models.CharField(max_length=100)),
                ('fansub', models.CharField(blank=True, max_length=100)),
                ('fsLink', models.CharField(blank=True, max_length=100)),
                ('ThumbnailFilename', models.UUIDField(default='31a672f0e6514a08bf4451345c43f372', editable=False, unique=True)),
                ('Thumbnail', models.ImageField(upload_to=animefly.utama.models.UploadToPathAndRename('media/thumbnail'))),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utama.anime')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeGenres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utama.anime')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utama.genres')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeEpisode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('server', models.CharField(default='', max_length=100)),
                ('link', models.CharField(default='', max_length=100)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utama.anime')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utama.episode')),
            ],
        ),
    ]
