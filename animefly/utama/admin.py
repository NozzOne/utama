import imp
from django.contrib import admin
from .models import Anime, Genres, AnimeGenres,  Episode, AnimeEpisode
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget


class AnimeEpisodeResource(resources.ModelResource):

    id = resources.Field(attribute='id')
    anime = resources.Field(attribute='anime', column_name='anime', widget=ForeignKeyWidget(Anime, 'id'))
    episode = resources.Field(attribute='episode', column_name='episode', widget=ForeignKeyWidget(Episode, 'id'))
    server = resources.Field(attribute='server', column_name='server')
    link = resources.Field(attribute='link', column_name='link')

    class Meta:
        model = AnimeEpisode
        import_id_fields = ('id','anime', 'episode')
        fields = ('id','anime', 'episode', 'server', 'link')

class AnimeEpisodeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("anime", "episode", "server", "link")
    search_fields = ("anime", "episode__id", "server", "link")
    list_per_page = 10
    resource_class = AnimeEpisodeResource


# Register your models here.
admin.site.register(Anime)
admin.site.register(Genres)
admin.site.register(AnimeGenres)
admin.site.register(Episode)
admin.site.register(AnimeEpisode, AnimeEpisodeAdmin)

