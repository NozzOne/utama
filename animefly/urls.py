"""animefly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from .utama import views


handler500 = "animefly.utama.views.error_500"
handler404 = "animefly.utama.views.error_404"
handler403 = "animefly.utama.views.error_403"


urlpatterns = [
    # admin
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    re_path(r'^chaining/', include('smart_selects.urls')),
    path('valeriko', admin.site.urls),

    # utama
    path('', views.home, name='home'),
    path('anime/<int:id>/<str:nombre>', views.anime, name='anime'),
    path('ver/<int:id>/<str:nombre>', views.ver, name='ver'),
    path('link', views.getServerLink, name='getServerlink'),
    path('directorio', views.directorio, name="directorio"),
    path('random', views.random, name="random"),
    path('notaccess', views.notaccess, name="notaccess"),
    path('broadcast', views.broadcast, name="broadcast"),

    # datas
    path('search', views.getdata, name="search"),
    path('iframe/<int:id>/<str:server>', views.getiframe, name="iframe"),

    # media
    path('media/render/<str:size>/<str:filename>', views.render_image, name='render'),
    path('media/background/<str:size>/<str:filename>', views.background_image, name='background'),
    path('media/cover/<str:size>/<str:filename>', views.cover_image, name='cover'),
    path('media/episode/<str:size>/<str:filename>', views.episode_image, name='episode'),

]
