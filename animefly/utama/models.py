from django.db import models
from uuid import uuid4
from django.utils.deconstruct import deconstructible
import os

# Create your models here.
@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = "webp"
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)

class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    titleEn = models.CharField(max_length=100)
    titleEs = models.CharField(max_length=100)
    description = models.TextField()
    tipo = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    release = models.DateField()
    rating = models.CharField(max_length=50)
    
    coverFilename = models.UUIDField(default=str(uuid4().hex), editable=False, unique=True)
    cover = models.ImageField(upload_to=UploadToPathAndRename('media/cover'))

    backgroundFilename = models.UUIDField(default=str(uuid4().hex), editable=False, unique=True)
    background = models.ImageField(upload_to=UploadToPathAndRename('media/background'))

    renderFilename = models.UUIDField(default=str(uuid4().hex), editable=False, unique=True)
    render = models.ImageField(upload_to=UploadToPathAndRename('media/render'))

    def __str__(self):
        return self.title      

class Genres(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class AnimeGenres(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)

    def __str__(self):
        return self.anime.title + ' - ' + self.genre.name

class Episode(models.Model):
    id = models.AutoField(primary_key=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    episode = models.IntegerField()
    title = models.CharField(max_length=100)
    titleEn = models.CharField(max_length=100)
    fansub = models.CharField(max_length=100, blank=True)
    fsLink = models.CharField(max_length=100, blank=True)
    ThumbnailFilename = models.UUIDField(default=str(uuid4().hex), editable=False, unique=True)
    Thumbnail = models.ImageField(upload_to=UploadToPathAndRename('media/thumbnail'))
    
    def __str__(self):
        return self.anime.title + ' - ' + str(self.episode) 

    
class AnimeEpisode(models.Model):
    id = models.AutoField(primary_key=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    # create server and link fields
    server = models.CharField(max_length=100, default='')
    link = models.CharField(max_length=100 , default='')



    def __str__(self):
        return self.anime.title + ' - ' + str(self.episode.episode)
    









