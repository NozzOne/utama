from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.http import FileResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.gis.geoip2 import GeoIP2

from .models import Anime, Genres, AnimeGenres,  Episode, AnimeEpisode


from PIL import Image
from io import BytesIO
from ipware import get_client_ip
from ..settings import GEOIP_PATH

def check_ip(request):
    client_ip, is_routable = get_client_ip(request)
    g = GeoIP2()
    if client_ip is None:
        # redirect
        return redirect('null')
    else:

        if g.country(client_ip)['country_code'] in ['MX', 'CO', 'ES', 'AR', 'PE', 'VE', 'CL', 'GT', 'EC', 'CU', 'BO', 'DO', 'HN','SV', 'PY', 'NI', 'CR', 'PA', 'PR', 'UY', 'BZ']:
            return redirect('home')
        else:
            return redirect('null')

# Create your views here.
def home(request):
    check_ip(request)
    MostPopular = Anime.objects.filter(rating__gte=8)[:5]
    episodios = Episode.objects.filter(is_premiere=1).order_by('-id')[0:12]
    Last_animes = Anime.objects.all().order_by('-id')[0:12]
    return render(request, 'utama/home.html', {'MostPopular': MostPopular, 'caps': episodios, 'series': Last_animes})

def anime(request, id, nombre=None):
    check_ip(request)
    anime = Anime.objects.get(id=id)
    episodios = Episode.objects.filter(anime_id=id).order_by('-id')
    count_episodes = Episode.objects.filter(anime_id=id).count()
    return render(request, 'utama/anime.html', {'anime': anime, 'capitulos': episodios, 'count': count_episodes})


def ver(request, id, nombre=None):
    check_ip(request)
    episode = Episode.objects.get(id=id)
    anime_episode = AnimeEpisode.objects.filter(episode_id=id).order_by('server')
    prev = Episode.objects.filter(anime__id=episode.anime_id).filter(id__lt=episode.id).order_by('-id')[0:1]
    sig = Episode.objects.filter(anime__id=episode.anime_id).filter(id__gt=episode.id).order_by('id')[0:1]

    return render(request, 'utama/ver.html', {'episode': episode, 'servers': anime_episode, 'prev': prev, 'sig': sig})

def notaccess(request):
    return render(request, 'utama/notaccess.html', {})

def random(request):
    check_ip(request)
    anime = Anime.objects.order_by('?').first()
    return redirect('/anime/'+str(anime.id)+'/'+anime.title)

def getServerLink(request):
    check_ip(request)
    if request.method == 'POST':
        id = request.POST['id']
        server = request.POST['server']
        anime_episode = AnimeEpisode.objects.filter(episode__id=id)
        return HttpResponse(anime_episode.get(server=server).link)


def getdata(request):
    check_ip(request)
    search = request.POST.get('search');
    animelist  = []
    if search != '':
        persons = Anime.objects.filter(Q(title__icontains=search) | Q(titleEn__icontains=search) | Q(titleEs__icontains=search))
    elif search == '':
        return JsonResponse({'animelist': animelist})
    for person in persons:
        animelist.append(
            {
                'slug'        :person.pk, 
                'title'      :person.title, 
                'titleEn'    :person.titleEn,
                'titleEs'    :person.titleEs,
                'description':person.description,
                'image'      :person.coverFilename,
                'tipo'     :person.tipo,
            }
        )

    return JsonResponse({'persons':animelist});


def directorio(request):
    check_ip(request)
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
    check_ip(request)
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
    check_ip(request)
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
    check_ip(request)
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
    check_ip(request)
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

