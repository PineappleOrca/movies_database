import pandas as pd
import os
import sqlite3 

def read_database()->pd.DataFrame:
    """
    Docstring for read_database
    :params: None
    :return: This is a general function which we can use to read in the entire movies database
    :rtype: pandas DataFrame
    """
    DB_FOLDER = "database"
    DB_NAME = os.path.join(DB_FOLDER, "movies.db")
    conn = sqlite3.connect(DB_NAME)
    query = """
    SELECT * FROM MOVIES;
    """
    return pd.read_sql_query(query, conn)

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
        
def get_currently_watching()->pd.DataFrame:
    '''
    Docstring for get_currently_watching
    :params: None
    :return: This function returns the dataframe for the content under the currently watching category. 
    :rtype: pandas DataFrame
    '''
    df = read_database()
    return df[df["watch_status"] == "Want To Watch"]


