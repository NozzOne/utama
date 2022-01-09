from django.shortcuts import render
from .models import Anime, Genres, AnimeGenres,  Episode, AnimeEpisode

from django.http import FileResponse


# Create your views here.
def home(request):
    MostPopular = Anime.objects.all().order_by('rating')[:5]
    episodios = Episode.objects.all().order_by('-id')[0:12]
    Last_animes = Anime.objects.all().order_by('-id')[0:12]
    return render(request, 'utama/home.html', {'MostPopular': MostPopular, 'caps': episodios, 'series': Last_animes})

def anime(request, id, nombre=None):
    # get anime
    anime = Anime.objects.get(id=id)
    episodios = Episode.objects.filter(anime_id=id).order_by('-id')
    count_episodes = Episode.objects.filter(anime_id=id).count()

    
    return render(request, 'utama/anime.html', {'anime': anime, 'capitulos': episodios, 'count': count_episodes})


def ver(request, id, nombre=None):
    episode = Episode.objects.get(id=id)
    anime_episode = AnimeEpisode.objects.filter(episode_id=id).order_by('server')
    # get previus episode
    prev = Episode.objects.filter(anime_id=episode.anime_id).filter(id__lt=episode.id).order_by('-id')[0:1]
    # get next episode
    next = Episode.objects.filter(anime_id=episode.anime_id).filter(id__gt=episode.id).order_by('id')[0:1]


    return render(request, 'utama/ver.html', {'episode': episode, 'servers': anime_episode, 'prev': prev, 'next': next})

def directorio(request):
    # genres order by name
    generos = Genres.objects.order_by('name')
    # Last_animes = AnimeCover.objects.select_related('anime', 'anime_genres').order_by('-id')[0:10]
    hola = "hola"
    return render(request, 'utama/directorio.html', {'generos': generos, 'series': hola})


def render_image(request, filename):
    path = Anime.objects.get(renderFilename=filename).render.path
    return FileResponse(open(path, 'rb'), content_type='image/webp')

def background_image(request, filename):
    path = Anime.objects.get(backgroundFilename=filename).background.path
    return FileResponse(open(path, 'rb'), content_type='image/webp')

def cover_image(request, filename):
    path = Anime.objects.get(coverFilename=filename).cover.path
    return FileResponse(open(path, 'rb'), content_type='image/webp')


def episode_image(request, filename):
    path = Episode.objects.get(ThumbnailFilename=filename).Thumbnail.path
    return FileResponse(open(path, 'rb'), content_type='image/webp')


def error_500(request, exception=None):
    return render(request, 'utama/500.html', {})

def error_404(request, exception):
    return render(request, 'utama/404.html', {})

def error_403(request, exception=None):
    return render(request, 'utama/403.html', {})

