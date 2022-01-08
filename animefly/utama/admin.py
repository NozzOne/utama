from django.contrib import admin
from .models import Anime, EpisodeThumbnail, Genres, AnimeGenres, AnimeCover, AnimeBackground, AnimeRender, Episode, AnimeEpisode

# Register your models here.
admin.site.register(Anime)
admin.site.register(Genres)
admin.site.register(AnimeGenres)
admin.site.register(AnimeCover)
admin.site.register(AnimeBackground)
admin.site.register(AnimeRender)
admin.site.register(Episode)
admin.site.register(AnimeEpisode)
admin.site.register(EpisodeThumbnail)
