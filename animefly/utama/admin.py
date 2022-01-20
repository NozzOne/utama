from django.contrib import admin
from .models import Anime, Genres, AnimeGenres,  Episode, AnimeEpisode
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class AnimeEpisodeResource(resources.ModelResource):

    anime_id = resources.Field(attribute='anime_id', column_name='anime_id')
    episode_id = resources.Field(attribute='episode_id', column_name='episode_id')
    server = resources.Field(attribute='server', column_name='server')
    link = resources.Field(attribute='link', column_name='link')

    class Meta:
        model = AnimeEpisode
        import_id_fields = ('anime_id', 'episode_id')
        fields = ('anime_id', 'episode_id', 'server', 'link')

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

