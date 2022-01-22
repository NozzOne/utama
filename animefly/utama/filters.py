import django_filters
from django.forms.widgets import Select

from .models import Anime, Genres



class AnimeFilter(django_filters.FilterSet):

    CHOICES = (
        ('alfabetico', 'Alfabetico'),
        ('alfabetico-desc', 'Alfabetico (desc)'),
        ('rating', 'Rating'),
        ('rating-desc', 'Rating (desc)'),
    )
    STATUS_CHOICES = (
        ('En Emisión', 'En Emisión'),
        ('Terminada', 'Terminada'),
        )

    TIPO_CHOICES = (
        ('Anime', 'Anime'),
        ('OVA', 'OVA'),
        ('ONA', 'ONA'),
        ('Película', 'Película'),
        )

    GENRE_CHOICES = [(genre.id, genre.name) for genre in Genres.objects.all()]

    ordering = django_filters.ChoiceFilter(label='Orden', choices=CHOICES, method='filter_by_ordering', empty_label='NINGUNO', widget=Select(attrs={'class':'select-style', 'onchange':'this.form.submit()'}))
    status = django_filters.ChoiceFilter(label='Status', choices=STATUS_CHOICES, method='filter_by_status', empty_label='TODOS LOS ESTADOS', widget=Select(attrs={'class':'select-style', 'onchange':'this.form.submit()'}))
    genres = django_filters.ChoiceFilter(label='Genero', choices=GENRE_CHOICES, method='filter_by_genre', empty_label='TODOS', widget=Select(attrs={'class':'select-style', 'onchange':'this.form.submit()'}))
    tipo = django_filters.ChoiceFilter(label='Tipo', choices=TIPO_CHOICES, method='filter_by_tipo', empty_label='TODOS LOS TIPOS', widget=Select(attrs={'class':'select-style', 'onchange':'this.form.submit()'}))

    class Meta:
        model = Anime
        fields = ['status', 'tipo', 'genres']


    def filter_by_tipo(self, queryset, name, value):
        if value == 'Anime':
            return queryset.filter(tipo='Anime')
        if value == 'OVA':
            return queryset.filter(tipo='OVA')
        if value == 'ONA':
            return queryset.filter(tipo='ONA')
        if value == 'Película':
            return queryset.filter(tipo='Película')

    def filter_by_genre(self, queryset, name, value):
        return queryset.filter(animegenres__genre__id=value)


    def filter_by_status(self, queryset, name, value):
        
        if value == 'En Emisión':
            return queryset.filter(status='En Emisión')
        if value == 'Terminada':
            return queryset.filter(status='Terminada')

    def filter_by_ordering(self, queryset, name, value):
        if value == 'alfabetico':
            return queryset.order_by('title')
        if value == 'alfabetico-desc':
            return queryset.order_by('-title')
        if value == 'rating':
            return queryset.order_by('rating')
        if value == 'rating-desc':
            return queryset.order_by('-rating')
