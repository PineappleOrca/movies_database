import pandas as pd 
import os
import sqlite3
from .get_dataframes import fetch_database
from .classes import ContentType, WatchStatus
# This is a repository of helper functions for statistics to be displayed

# Global variables to locate the databases
DB_FOLDER = "database"
DB_NAME = os.path.join(DB_FOLDER, "movies.db")

def get_sum(df: pd.DataFrame)->int:
    '''
    This function returns the number of times something has been watched
    Input: Pandas dataframe
    '''
    if df.empty:
        return 0
    else:
        return df['times_watched'].sum()

def get_most_watched_movie()->str:
    '''
    This function when called returns the most frequently watched movie name as a string
    '''
    try:
        with sqlite3.connect(DB_NAME) as conn:
            query = """
            SELECT title
            FROM movies
            WHERE content_type = 'Movie'
            ORDER BY times_watched DESC
            LIMIT 1;
            """
            df = pd.read_sql_query(query, conn)
            last_title = "No Movies have been watched!"
            if not df.empty:
                last_title = df.iloc[0]['title']
            return last_title
    except:
        return "No content has been watched yet!"

def get_total_watched_episodes()->int:
    '''
    Docstring for get_total_watched_episodes
    
    :return: returns the total count of all watched episodes for series.
    :rtype: int
    '''
    try:
        with sqlite3.connect(DB_NAME) as conn:
            query = """SELECT * FROM movies"""
            df = pd.read_sql_query(query, conn)
            df = df[df['content_type'] == ContentType.SERIES.value]
            df = df[(df['watch_status'] == WatchStatus.CURRENT.value) | (df['watch_status'] == WatchStatus.WATCHED.value) | (df['watch_status'] == WatchStatus.DROP.value)]
            df['total'] = df['times_watched']*df['episodes_watched']
            return df['total'].sum() if not df.empty else 0
    except:
        return 0

def get_most_watched_movie_count()->int:
    '''
    Docstring for get_most_watched_movie_count
    
    :return: Returns the times_watched for the most_watched movie 
    :rtype: int
    '''
    try: 
        with sqlite3.connect(DB_NAME) as conn:
            query = """SELECT * FROM movies"""
            df = pd.read_sql_query(query, conn)
            most_watched_movie = get_most_watched_movie()
            df = df[df['title'] == most_watched_movie]
            return df['times_watched'].iloc[0] if not df.empty else 0
    except:
        return 0