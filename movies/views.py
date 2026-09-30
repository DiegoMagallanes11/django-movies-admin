from django.shortcuts import render
from .models import Movie, Genre


def recommendations(request):
    genre_id = request.GET.get('genre')
    genres = Genre.objects.all()
    selected_genre = None
    movies = []

    if genre_id:
        try:
            selected_genre = Genre.objects.get(pk=genre_id)
            movies = selected_genre.movies.all()
        except Genre.DoesNotExist:
            pass
    else:
        movies = Movie.objects.all()

    movies_with_ratings = []
    for movie in movies:
        avg = movie.average_rating
        movies_with_ratings.append({
            'movie': movie,
            'average_rating': avg if avg is not None else 0,
        })

    movies_with_ratings.sort(key=lambda x: x['average_rating'], reverse=True)

    context = {
        'genres': genres,
        'selected_genre': selected_genre,
        'recommendations': movies_with_ratings,
    }
    return render(request, 'movies/recommendations.html', context)
