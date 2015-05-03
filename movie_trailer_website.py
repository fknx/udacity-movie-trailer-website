from datetime import date
import fresh_tomatoes

class Movie(object):
    """Stores information about a movie."""
    def __init__(self, title, poster_image_url, trailer_youtube_url, lead_actors, release_date):
        """Creates a new Movie instance.

        Args:
            title: The title of the movie.
            poster_image_url: The URL to the movie's poster image.
            trailer_youtube_url: The URL of the movie's youtube trailer.
            lead_actors: The movie's lead actors.
            release_date: The movie's release date.
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.lead_actors = lead_actors
        self.release_date = release_date

movies = []

# The Dark Knight

movies.append(Movie(
    'The Dark Knight',
    'http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY317_CR0,0,214,317_AL_.jpg',
    'https://www.youtube.com/watch?v=EXeTwQWrcwY',
    ['Christian Bale', 'Heath Ledger', 'Aaron Eckhart'],
    date(2008, 07, 18)
))

# Interstellar

movies.append(Movie(
    'Interstellar',
    'http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX214_AL_.jpg',
    'https://www.youtube.com/watch?v=2LqzF5WauAw',
    ['Matthew McConaughey', 'Anne Hathaway', 'Jessica Chastain'],
    date(2014, 11, 07)
))

# Inception

movies.append(Movie(
    'Inception',
    'http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX214_AL_.jpg',
    'https://www.youtube.com/watch?v=8hP9D6kZseM',
    ['Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Ellen Page'],
    date(2010, 07, 16)
))

# Kung Fu Hustle

movies.append(Movie(
    'Kung Fu Hustle',
    'http://ia.media-imdb.com/images/M/MV5BMjQwNTMwODU0Ml5BMl5BanBnXkFtZTcwODkzNjgyMQ@@._V1_SY317_CR0,0,214,317_AL_.jpg',
    'https://www.youtube.com/watch?v=-m3IB7N_PRk',
    ['Stephen Chow', 'Wah Yuen', 'Qiu Yuen'],
    date(2005, 04, 22)
))

# Shaolin Soccer

movies.append(Movie(
    'Shaolin Soccer',
    'http://ia.media-imdb.com/images/M/MV5BMTk3NDg5NTE4MV5BMl5BanBnXkFtZTcwNzMxMjAwMQ@@._V1_SY317_CR1,0,214,317_AL_.jpg',
    'https://www.youtube.com/watch?v=6FAaOwNnHTA',
    ['Stephen Chow, Wei Zhao, Yat-Fei Wong'],
    date(2001, 07, 12)
))

# The Lord of the Rings: The Two Towers

movies.append(Movie(
    'The Lord of the Rings: The Two Towers',
    'http://ia.media-imdb.com/images/M/MV5BMTAyNDU0NjY4NTheQTJeQWpwZ15BbWU2MDk4MTY2Nw@@._V1_SY317_CR1,0,214,317_AL_.jpg',
    'https://www.youtube.com/watch?v=cvCktPUwkW0',
    ['Elijah Wood', 'Ian McKellen', 'Viggo Mortensen'],
    date(2002, 12, 18)
))

# create and open the movie trailer website
fresh_tomatoes.open_movies_page(movies)