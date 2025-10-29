import pandas as pd

def get_content_df(df, flag):
    match flag:
        case 'Movies':
            return df[(df['content_type'] == 'Movie')]
        case 'Series':
            return df[(df['content_type'] == 'Series')]
        case 'Book':
            return df[(df['content_type'] == 'Book')]
        case _:
            raise Exception("Please enter a value from Movies/Series/Book")

def get_movie_genre_df(df, flag):
    # need to add a check to make sure the correct pandas df is being sent to this function
   # if df['content_type'] != 'Movie':
   #     raise Exception("Please submit the movies dataframe! The incorrect dataframe was parsed")
    match flag:
        case 'Horror':
            return df[df['genre'] == 'Horror']
        case 'Animated':
            return df[df['genre'] == 'Animated']
        case 'Other':
            return df[df['genre'] == 'Other']
        case _:
            raise Exception("Please enter a flag from Horror/Animated/Other")
