from django.contrib import admin
from .models import Anime, Episode_thumbnail, Genres, Anime_genre, Anime_cover, Anime_background, Anime_render, Episode, Anime_episode

# Register your models here.
admin.site.register(Anime)
admin.site.register(Genres)
admin.site.register(Anime_genre)
admin.site.register(Anime_cover)
admin.site.register(Anime_background)
admin.site.register(Anime_render)
admin.site.register(Episode)
admin.site.register(Anime_episode)
admin.site.register(Episode_thumbnail)
