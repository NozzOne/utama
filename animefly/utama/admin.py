from django.contrib import admin
from .models import Anime, Genres, AnimeGenres,  Episode, AnimeEpisode

# Register your models here.
admin.site.register(Anime)
admin.site.register(Genres)
admin.site.register(AnimeGenres)
admin.site.register(Episode)
admin.site.register(AnimeEpisode)

