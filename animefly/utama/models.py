from django.db import models
from uuid import uuid4

# Create your models here.
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

    def __str__(self):
        return self.title      


class Genres(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Anime_genre(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)

    def __str__(self):
        return self.anime.title + ' - ' + self.genre.name

class Anime_cover(models.Model):
    filename = models.UUIDField(default=str(uuid4().hex), editable=False, unique=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='media/cover', verbose_name=filename)

    def __str__(self):
        return self.anime.title

class Anime_background(models.Model):
    filename = models.UUIDField(default=str(uuid4().hex), editable=False, unique=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    background = models.ImageField(upload_to='media/background', verbose_name=filename)

    def __str__(self):
        return self.anime.title

class Anime_render(models.Model):
    filename = models.UUIDField(default=str(uuid4().hex), editable=False, unique=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    render = models.ImageField(upload_to='media/render', verbose_name=filename)

    def __str__(self):
        return self.anime.title

class Episode(models.Model):
    id = models.AutoField(primary_key=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    episode = models.IntegerField()
    title = models.CharField(max_length=100)
    titleEn = models.CharField(max_length=100)
    fansub = models.CharField(max_length=100, blank=True)
    fsLink = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.anime.title + ' - ' + str(self.episode) 
    
class Episode_thumbnail(models.Model):
    filename = models.UUIDField(default=str(uuid4().hex), editable=False, unique=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='media/thumbnail', verbose_name=filename)

    def __str__(self):
        return self.episode.anime.title + ' - ' + str(self.episode.episode)

class Anime_episode(models.Model):
    id = models.AutoField(primary_key=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    # create server and link fields
    server = models.CharField(max_length=100, default='')
    link = models.CharField(max_length=100 , default='')



    def __str__(self):
        return self.anime.title + ' - ' + str(self.episode.episode)
    









