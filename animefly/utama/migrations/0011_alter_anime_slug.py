# Generated by Django 4.0.1 on 2022-01-17 05:10

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utama', '0010_remove_anime_description_anime_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
