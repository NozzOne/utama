
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import FileResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

from .models import Anime, Genres, AnimeGenres,  Episode, AnimeEpisode


from PIL import Image
from io import BytesIO
# Create your views here.
def home(request):
    MostPopular = Anime.objects.filter(rating__gte=8)[:5]
    episodios = Episode.objects.filter(is_premiere=1).order_by('-id')[0:12]
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
    prev = Episode.objects.filter(anime_id=episode.anime_id).filter(id__lt=episode.id).order_by('-id')[0:1]
    next = Episode.objects.filter(anime_id=episode.anime_id).filter(id__gt=episode.id).order_by('id')[0:1]
    return render(request, 'utama/ver.html', {'episode': episode, 'servers': anime_episode, 'prev': prev, 'next': next})

def random(request):
    return render(request, 'utama/anime.html', {'anime': anime, 'capitulos': episodios, 'count': count_episodes})


@csrf_exempt
def getServerLink(request):
    if request.method == 'POST':
        # get data from post
        id = request.POST['id']
        server = request.POST['server']
        anime_episode = AnimeEpisode.objects.filter(episode__id=id)
        return HttpResponse(anime_episode.get(server=server).link)






def directorio(request):
    
    animes = Anime.objects.all()
    genres = Genres.objects.all().order_by('name')

    # Pagination animes list
    paginator = Paginator(animes, 12)
    page = request.GET.get('page')
    try:
        animes = paginator.page(page)
    except PageNotAnInteger:
        animes = paginator.page(1)
    except EmptyPage:
        animes = paginator.page(paginator.num_pages)




    return render(request, 'utama/directorio.html', {'generos': genres, 'animes': animes})


def render_image(request, size,filename):
    small = (200,200)
    medium = (400,400)
    large = (600,600)
    xlarge = (800,800)
    xxlarge = (1000,1000)
    xxxlarge = (1200,1200)
    path = Anime.objects.get(renderFilename=filename).render.path
    image = Image.open(path)
    if size == 'small':
        image.thumbnail(small)
    elif size == 'medium':
        image.thumbnail(medium)
    elif size == 'large':
        image.thumbnail(large)
    elif size == 'xlarge':
        image.thumbnail(xlarge)
    elif size == 'xxlarge':
        image.thumbnail(xxlarge)
    elif size == 'xxxlarge':
        image.thumbnail(xxxlarge)
    # save image in memory
    img_io = BytesIO()
    image.save(img_io, 'WEBP', quality=90)
    img_io.seek(0)
    return FileResponse(img_io, content_type='image/webp')


def background_image(request, size,filename):
    small = (200,200)
    medium = (400,400)
    large = (600,600)
    xlarge = (800,800)
    xxlarge = (1000,1000)
    xxxlarge = (1200,1200)
    path = Anime.objects.get(backgroundFilename=filename).background.path
    image = Image.open(path)
    if size == 'small':
        image.thumbnail(small)
    elif size == 'medium':
        image.thumbnail(medium)
    elif size == 'large':
        image.thumbnail(large)
    elif size == 'xlarge':
        image.thumbnail(xlarge)
    elif size == 'xxlarge':
        image.thumbnail(xxlarge)
    elif size == 'xxxlarge':
        image.thumbnail(xxxlarge)
    
    # save image in memory
    img_io = BytesIO()
    image.save(img_io, 'WEBP', quality=90)
    img_io.seek(0)
    return FileResponse(img_io, content_type='image/webp')

def cover_image(request, size,filename):
    small = (200,200)
    medium = (400,400)
    large = (600,600)
    xlarge = (800,800)
    xxlarge = (1000,1000)
    xxxlarge = (1200,1200)
    path = Anime.objects.get(coverFilename=filename).cover.path
    image = Image.open(path)
    if size == 'small':
        image.thumbnail(small)
    elif size == 'medium':
        image.thumbnail(medium)
    elif size == 'large':
        image.thumbnail(large)
    elif size == 'xlarge':
        image.thumbnail(xlarge)
    elif size == 'xxlarge':
        image.thumbnail(xxlarge)
    elif size == 'xxxlarge':
        image.thumbnail(xxxlarge)
    
    # save image in memory
    img_io = BytesIO()
    image.save(img_io, 'WEBP', quality=90)
    img_io.seek(0)
    return FileResponse(img_io, content_type='image/webp')


def episode_image(request, size,filename):

    small = (200,200)
    medium = (400,400)
    large = (600,600)
    xlarge = (800,800)
    xxlarge = (1000,1000)
    xxxlarge = (1200,1200)
    path = Episode.objects.get(ThumbnailFilename=filename).Thumbnail.path
    image = Image.open(path)
    if size == 'small':
        image.thumbnail(small)
    elif size == 'medium':
        image.thumbnail(medium)
    elif size == 'large':
        image.thumbnail(large)
    elif size == 'xlarge':
        image.thumbnail(xlarge)
    elif size == 'xxlarge':
        image.thumbnail(xxlarge)
    elif size == 'xxxlarge':
        image.thumbnail(xxxlarge)
    
    # save image in memory
    img_io = BytesIO()
    image.save(img_io, 'WEBP', quality=90)
    img_io.seek(0)
    return FileResponse(img_io, content_type='image/webp')

def error_500(request, exception=None):
    return render(request, 'utama/500.html', {})

def error_404(request, exception):
    return render(request, 'utama/404.html', {})

def error_403(request, exception=None):
    return render(request, 'utama/403.html', {})

