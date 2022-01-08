from django.shortcuts import render
from .models import Anime, EpisodeThumbnail, Genres, AnimeGenres, AnimeCover, AnimeBackground, AnimeRender, Episode, AnimeEpisode

from django.http import FileResponse


# Create your views here.
def home(request):
    MostPopular = AnimeBackground.objects.select_related('anime').order_by('-id')[:5]
    episodios = EpisodeThumbnail.objects.select_related('episode').order_by('-id')[0:12]
    Last_animes = AnimeCover.objects.select_related('anime').order_by('-id')[0:10]
    return render(request, 'utama/home.html', {'MostPopular': MostPopular, 'caps': episodios, 'series': Last_animes})

def anime(request, id, nombre=None):
    anime = Anime.objects.get(id=id)
    anime_genres = AnimeGenres.objects.filter(anime_id=id)
    RenderAnime = AnimeRender.objects.get(anime_id=id).filename
    episodios = EpisodeThumbnail.objects.select_related('episode').filter(episode__anime=id).order_by('-id')[0:12]
    count_episodes = Episode.objects.filter(anime_id=id).count()
    return render(request, 'utama/anime.html', {'anime': anime, 'capitulos': episodios, 'generos': anime_genres, 'render': RenderAnime, 'count': count_episodes})


def ver(request, id, nombre=None):
    episode = Episode.objects.get(id=id)
    anime_episode = AnimeEpisode.objects.filter(episode_id=id).order_by('server')
    return render(request, 'utama/ver.html', {'episode': episode, 'servers': anime_episode})


def render_image(request, filename):
    path = AnimeRender.objects.get(filename=filename).render.path
    return FileResponse(open(path, 'rb'), content_type='image/webp')

def background_image(request, filename):
    path = AnimeBackground.objects.get(filename=filename).background.path
    return FileResponse(open(path, 'rb'), content_type='image/webp')

def cover_image(request, filename):
    path = AnimeCover.objects.get(filename=filename).cover.path
    return FileResponse(open(path, 'rb'), content_type='image/webp')


def episode_image(request, filename):
    path = EpisodeThumbnail.objects.get(filename=filename).thumbnail.path
    return FileResponse(open(path, 'rb'), content_type='image/webp')