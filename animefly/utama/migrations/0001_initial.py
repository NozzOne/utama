# Generated by Django 4.0.1 on 2022-01-07 21:57

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
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utama.anime')),
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
            name='EpisodeThumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.UUIDField(default='eeddac87d1a34485aee5f2db5bb0ebd1', editable=False, unique=True)),
                ('thumbnail', models.ImageField(upload_to='media/thumbnail', verbose_name=models.UUIDField(default='eeddac87d1a34485aee5f2db5bb0ebd1', editable=False, unique=True))),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utama.episode')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeRender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.UUIDField(default='05e95de81649429f9e110a62a1425d61', editable=False, unique=True)),
                ('render', models.ImageField(upload_to='media/render', verbose_name=models.UUIDField(default='05e95de81649429f9e110a62a1425d61', editable=False, unique=True))),
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
        migrations.CreateModel(
            name='AnimeCover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.UUIDField(default='013f616ca52745e9b79882ae733dac50', editable=False, unique=True)),
                ('cover', models.ImageField(upload_to='media/cover', verbose_name=models.UUIDField(default='013f616ca52745e9b79882ae733dac50', editable=False, unique=True))),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utama.anime')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.UUIDField(default='d9b844bd5110467e9ff07156e4261a9a', editable=False, unique=True)),
                ('background', models.ImageField(upload_to='media/background', verbose_name=models.UUIDField(default='d9b844bd5110467e9ff07156e4261a9a', editable=False, unique=True))),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utama.anime')),
            ],
        ),
    ]
