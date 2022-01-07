from django.shortcuts import render
from .models import Anime, Genres, Anime_genre, Anime_cover, Anime_background, Anime_render, Episode, Anime_episode, Episode_thumbnail
from django.http import FileResponse


# Create your views here.
def home(request):
    MostPopular = Anime_background.objects.select_related('anime').order_by('-id')[:5]
    episodios = Episode_thumbnail.objects.select_related('episode').order_by('-id')[0:12]
    Last_animes = Anime_cover.objects.select_related('anime').order_by('-id')[0:10]


    return render(request, 'utama/home.html', {'MostPopular': MostPopular, 'caps': episodios, 'series': Last_animes})

def anime(request, id, nombre=None):
    anime = Anime.objects.get(id=id)
    anime_genres = Anime_genre.objects.filter(anime_id=id)
    anime_render = Anime_render.objects.get(anime_id=id).filename
    episodios = Episode_thumbnail.objects.select_related('episode').order_by('-id')
    count_episodes = Episode.objects.filter(anime_id=id).count()
    return render(request, 'utama/anime.html', {'anime': anime, 'capitulos': episodios, 'generos': anime_genres, 'render': anime_render, 'count': count_episodes})

def ver(request, id, nombre=None):
    episode = Episode.objects.get(id=id)
    anime_episode = Anime_episode.objects.filter(episode_id=id)


    return render(request, 'utama/ver.html', {'episode': episode, 'servers': anime_episode})


def render_image(request, filename):
    path = Anime_render.objects.get(filename=filename).render.path
    return FileResponse(open(path, 'rb'), content_type='image/webp')

def background_image(request, filename):
    path = Anime_background.objects.get(filename=filename).background.path
    return FileResponse(open(path, 'rb'), content_type='image/webp')

def cover_image(request, filename):
    path = Anime_cover.objects.get(filename=filename).cover.path
    return FileResponse(open(path, 'rb'), content_type='image/webp')


def episode_image(request, filename):
    path = Episode_thumbnail.objects.get(filename=filename).thumbnail.path
    return FileResponse(open(path, 'rb'), content_type='image/webp')