from django.core.management.base import BaseCommand
from movies.models import Movie, Genre, Person, Rating


class Command(BaseCommand):
    help = 'Load test data for the movies app'

    def handle(self, *args, **options):
        self.stdout.write('Loading test data...')

        action = Genre.objects.create(name='Action')
        comedy = Genre.objects.create(name='Comedy')
        drama = Genre.objects.create(name='Drama')
        scifi = Genre.objects.create(name='Science Fiction')

        nolan = Person.objects.create(first_name='Christopher', last_name='Nolan')
        spielberg = Person.objects.create(first_name='Steven', last_name='Spielberg')
        tarantino = Person.objects.create(first_name='Quentin', last_name='Tarantino')

        m1 = Movie.objects.create(title='Inception', year=2010, director=nolan)
        m1.genres.set([action, scifi])

        m2 = Movie.objects.create(title='The Dark Knight', year=2008, director=nolan)
        m2.genres.set([action, drama])

        m3 = Movie.objects.create(title='Interstellar', year=2014, director=nolan)
        m3.genres.set([scifi, drama])

        m4 = Movie.objects.create(title='Pulp Fiction', year=1994, director=tarantino)
        m4.genres.set([drama])

        m5 = Movie.objects.create(title='Django Unchained', year=2012, director=tarantino)
        m5.genres.set([drama, action])

        m6 = Movie.objects.create(title='Jurassic Park', year=1993, director=spielberg)
        m6.genres.set([action, scifi])

        m7 = Movie.objects.create(title='Schindlers List', year=1993, director=spielberg)
        m7.genres.set([drama])

        m8 = Movie.objects.create(title='The Terminal', year=2004, director=spielberg)
        m8.genres.set([comedy, drama])

        m9 = Movie.objects.create(title='Catch Me If You Can', year=2002, director=spielberg)
        m9.genres.set([comedy, drama])

        m10 = Movie.objects.create(title='Tenet', year=2020, director=nolan)
        m10.genres.set([action, scifi])

        Rating.objects.create(movie=m1, reviewer=nolan, stars=5, comment='Mind-bending masterpiece')
        Rating.objects.create(movie=m1, reviewer=spielberg, stars=4, comment='Great visuals')
        Rating.objects.create(movie=m2, reviewer=nolan, stars=5, comment='Best superhero film')
        Rating.objects.create(movie=m2, reviewer=tarantino, stars=5, comment='Heath Ledger is legendary')
        Rating.objects.create(movie=m3, reviewer=spielberg, stars=4, comment='Emotional and epic')
        Rating.objects.create(movie=m4, reviewer=tarantino, stars=5, comment='Classic dialogue')
        Rating.objects.create(movie=m5, reviewer=nolan, stars=4, comment='Great western')
        Rating.objects.create(movie=m6, reviewer=spielberg, stars=4, comment='Iconic dinosaurs')
        Rating.objects.create(movie=m7, reviewer=nolan, stars=5, comment='Powerful and moving')
        Rating.objects.create(movie=m8, reviewer=spielberg, stars=3, comment='Charming but slow')
        Rating.objects.create(movie=m9, reviewer=tarantino, stars=4, comment='Fun and stylish')
        Rating.objects.create(movie=m10, reviewer=nolan, stars=4, comment='Complex but rewarding')

        self.stdout.write(self.style.SUCCESS('Test data loaded successfully!'))
        self.stdout.write(f'  - {Genre.objects.count()} genres')
        self.stdout.write(f'  - {Person.objects.count()} people')
        self.stdout.write(f'  - {Movie.objects.count()} movies')
        self.stdout.write(f'  - {Rating.objects.count()} ratings')
