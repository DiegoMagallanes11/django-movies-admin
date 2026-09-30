from django.contrib import admin
from .models import Movie, Genre, Person, Rating


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'director', 'average_rating', 'created_at')
    list_filter = ('genres', 'year')
    search_fields = ('title', 'director__first_name', 'director__last_name')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [RatingInline]
    filter_horizontal = ('genres',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'movie_count', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')

    def movie_count(self, obj):
        return obj.movies.count()
    movie_count.short_description = 'Movies'


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created_at')
    search_fields = ('first_name', 'last_name')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'reviewer', 'stars', 'created_at')
    list_filter = ('stars', 'movie')
    search_fields = ('movie__title', 'reviewer__first_name', 'reviewer__last_name')
    readonly_fields = ('created_at', 'updated_at')
