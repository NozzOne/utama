# Generated by Django 4.0.1 on 2022-01-09 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utama', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='backgroundFilename',
            field=models.UUIDField(default='a99995e5929b4db2b50774d5c896853d', editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='coverFilename',
            field=models.UUIDField(default='539bd3d4204f43e880a128d75d0fcb82', editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='renderFilename',
            field=models.UUIDField(default='f4aff92e3ab543ffa689b65a0aaab65a', editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='ThumbnailFilename',
            field=models.UUIDField(default='7680b6f0ec90472590089d850d7dd456', editable=False, unique=True),
        ),
    ]
