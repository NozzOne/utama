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
    # get cover with anime id
    cover = AnimeCover.objects.get(anime_id=id).filename

    return render(request, 'utama/anime.html', {'anime': anime, 'capitulos': episodios, 'generos': anime_genres, 'render': RenderAnime, 'count': count_episodes, 'cover': cover})


def ver(request, id, nombre=None):
    episode = Episode.objects.get(id=id)
    anime_episode = AnimeEpisode.objects.filter(episode_id=id).order_by('server')
    # get previus episode
    prev = Episode.objects.filter(anime_id=episode.anime_id).filter(id__lt=episode.id).order_by('-id')[0:1]
    # get next episode
    next = Episode.objects.filter(anime_id=episode.anime_id).filter(id__gt=episode.id).order_by('id')[0:1]
    # obtener animes con categoria similar
    # anime_genres = AnimeGenres.objects.select_related('genre').filter(anime_id=episode.anime_id)
    # similar = [i.genre.id for i in anime_genres][0]
    # # get anime similar
    # anime_similar = AnimeGenres.objects.filter(genre=similar).exclude(anime_id=episode.anime_id).distinct()[0:5]

    return render(request, 'utama/ver.html', {'episode': episode, 'servers': anime_episode, 'prev': prev, 'next': next})

def directorio(request):
    # genres order by name
    generos = Genres.objects.order_by('name')
    return render(request, 'utama/directorio.html', {'generos': generos})

def directorio_genero(request, id, nombre=None):
    genero = Genres.objects.get(id=id)
    animes = AnimeGenres.objects.select_related('anime').filter(genre=genero).order_by('-id')
    return render(request, 'utama/directorio.html', {'animes': animes, 'genero': genero})

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


def error_500(request, exception=None):
    return render(request, 'utama/500.html', {})

def error_404(request, exception):
    return render(request, 'utama/404.html', {})

def error_403(request, exception=None):
    return render(request, 'utama/403.html', {})

