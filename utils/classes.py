from enum import Enum

class ContentType(Enum):
    MOVIE = 'Movie'
    SERIES = 'Series'
    BOOK = 'Book'

class MovieGenre(Enum):
    HORROR = 'Horror'
    ANIMATION = 'Animation'
    OTHER = 'Other'

class SeriesGenre(Enum):
    ANIME = 'Anime'
    OTHER = 'Other'

class BookGenre(Enum):
    THRILLER = 'Thriller'
    ROMANCE = 'Romance'
    MYSTERY = 'Mystery'

class WatchStatus(Enum):
    CURRENT = 'Currently Watching'
    WATCHED = 'Watched'
    WISH = 'Want To Watch'
    DROP = 'Dropped'