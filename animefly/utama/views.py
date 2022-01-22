from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.http import FileResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.urls import reverse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template import Template, Context
from django.template.loader import get_template

from .models import Anime, AnimeGenres,  Episode, AnimeEpisode
from .filters import AnimeFilter
from .getter import *

from PIL import Image
from io import BytesIO
import datetime



def ckct(old_function):
    def new_function(request, id=None, nombre=None):
        country = request.META.get('HTTP_CF_IPCOUNTRY') 
        # if country not in ["AR","BO","CL","CO","CR","DO","EC","GT","HN","MX","NI","PA","PE","PR","PY","SV","UY","VE","ES"]:
        #     return redirect('notaccess')
        # else:
        if id and nombre:
            return old_function(request, id, nombre)
        else:
            return old_function(request)

    return new_function

# Create your views here.
@ckct
def home(request):
    MostPopular = Anime.objects.filter(rating__gte=8)[:5]
    episodios = Episode.objects.filter(is_premiere=1).order_by('-id')[0:12]
    Last_animes = Anime.objects.all().order_by('-id')[0:12]
    return render(request, 'utama/home.html', {'MostPopular': MostPopular, 'caps': episodios, 'series': Last_animes})

@ckct
def anime(request, id, nombre=None):
    anime = Anime.objects.get(id=id)
    episodios = Episode.objects.filter(anime_id=id).order_by('-id')
    count_episodes = Episode.objects.filter(anime_id=id).count()
    return render(request, 'utama/anime.html', {'anime': anime, 'capitulos': episodios, 'count': count_episodes})

@ckct
def ver(request, id, nombre=None):
    episode = Episode.objects.get(id=id)
    anime_episode = AnimeEpisode.objects.filter(episode_id=id).order_by('server')
    prev = Episode.objects.filter(anime__id=episode.anime_id).filter(id__lt=episode.id).order_by('-id')[0:1]
    sig = Episode.objects.filter(anime__id=episode.anime_id).filter(id__gt=episode.id).order_by('id')[0:1]

    return render(request, 'utama/ver.html', {'episode': episode, 'servers': anime_episode, 'prev': prev, 'sig': sig})

def notaccess(request):
    return render(request, 'utama/notaccess.html', {})
@ckct
def random(request):
    anime = Anime.objects.order_by('?').first()
    return redirect('/anime/'+str(anime.id)+'/'+anime.slug)

def getServerLink(request):
    if request.method == 'POST':
        id = request.POST['id']
        server = request.POST['server']
        anime_episode = AnimeEpisode.objects.filter(episode__id=id)
        link = anime_episode.get(server=server).link
        if "solidfiles" in link or "archive" in link:
            return HttpResponse('https://utama.live/iframe/'+id+"/"+server)
        return HttpResponse(link)

@xframe_options_exempt
def getiframe(request,id, server):
    anime = AnimeEpisode.objects.filter(episode__id=id)
    link = anime.get(server=server).link
    thumbnail = anime.get(server=server).episode.ThumbnailFilename
    
    if "fembed" in link:
        link = Fembed(url=link).fetch()
    
    elif "solidfiles" in link:
        link = SolidFiles(url=link).fetch()
    elif "mixdrop" in link:
        link = MixDrop(url=link).fetch()

    view = get_template('utama/iframe.html')
    context = {
        'link': link,
        'poster': thumbnail,
    }
    return HttpResponse(view.render(context, request))


def getdata(request):
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
                'image'      :person.coverFilename,
                'tipo'     :person.tipo,
            }
        )

    return JsonResponse({'persons':animelist});


def getfilter(request):
    r = request.POST

    animelist = []
    if r.get('tipo') == 'categoria' and r.get('search') != '':
        animes = AnimeGenres.objects.filter(genre__name="%s" % r.get('search'))
        
    for anime in animes:
        animelist.append(
            {
                'slug'       :anime.anime.pk,
                'title'      :anime.anime.title, 
                'fix'        :f"{anime.anime.title}".replace(" ", "-"),
                'image'      :anime.anime.coverFilename,
                'tipo'       :anime.anime.tipo,
                'status'     :anime.anime.status,
                'rating'     :anime.anime.rating,
            }
        )
    return JsonResponse({'animelist': animelist})

@ckct
def directorio(request):


    ids = list(AnimeGenres.objects.values_list('anime', flat=True).distinct())
    animes = Anime.objects.filter(id__in=ids)

    Animesfilter = AnimeFilter(request.GET, queryset=animes)
    animes = Animesfilter.qs
    paginator = Paginator(animes, 20)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(request, 'utama/directorio.html', {'filter_form': Animesfilter, 'filter': response})

@ckct
def broadcast(request):
    animes = Anime.objects.filter(status='En Emisión')

    for i in animes:
        # counts episodes 
        episodes = Episode.objects.filter(anime_id=i.id).count()
        i.release = i.release + datetime.timedelta(weeks=episodes)

    return render(request, 'utama/broadcast.html', {'animes': animes})



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
    return redirect('home')

def error_404(request, exception):
    return render(request, template_name='utama/404.html', status=404)

def error_403(request, exception=None):
    return render(request, 'utama/403.html', status=403)

