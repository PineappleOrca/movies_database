import pandas as pd

def get_content_df(df: pd.DataFrame, flag:str)->pd.DataFrame:
    match flag:
        case 'Movies':
            return df[(df['content_type'] == 'Movie')]
        case 'Series':
            return df[(df['content_type'] == 'Series')]
        case 'Book':
            return df[(df['content_type'] == 'Book')]
        case _:
            raise Exception("Please enter a value from Movies/Series/Book")

def get_movie_genre_df(df: pd.DataFrame, flag: str)->pd.core.frame.DataFrame:
    # need to add a check to make sure the correct pandas df is being sent to this function
   # if df['content_type'] != 'Movie':
   #     raise Exception("Please submit the movies dataframe! The incorrect dataframe was parsed")
    match flag:
        case 'Horror':
            return df[df['genre'] == 'Horror']
        case 'Animated':
            return df[df['genre'] == 'Animation']
        case 'Other':
            return df[df['genre'] == 'Other']
        case _:
            raise Exception("Please enter a flag from Horror/Animated/Other")
        
def get_series_genre_df(df: pd.DataFrame, flag: str)->pd.DataFrame:
    match flag:
        case 'Anime':
            return df[df['genre'] == 'Anime']
        case 'Other':
            return df[df['genre'] == 'Other']
        case _:
            raise Exception("Please enter a flag from Anime/Other")
        
def get_book_genre_df(df: pd.DataFrame, flag: str)-> pd.DataFrame:
    match flag:
        case 'Thriller':
            return df[df['genre'] == 'Thriller']
        case 'Mystery':
            return df[df['genre'] == 'Mystery']
        case _:
            raise Exception("Please enter a flag from Thriller or Mystery")
