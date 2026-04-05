import pandas as pd
import os
import sqlite3 
from utils.classes import ContentType, MovieGenre, SeriesGenre, BookGenre, WatchStatus
import logging 

# Initialise the logger
logging = logging.getLogger(__name__)

def read_database()->pd.DataFrame:
    """
    Docstring for read_database
    :params: None
    :return: This is a general function which we can use to read in the entire movies database
    :rtype: pandas DataFrame
    """
    DB_FOLDER = "database"
    DB_NAME = os.path.join(DB_FOLDER, "movies.db")
    try:
        with sqlite3.connect(DB_NAME) as conn:
            query = """SELECT * FROM MOVIES;"""
    except Exception as e:
        logging.info(f"Unexpected Error found: {e}!")
    else:
        logging.info("Fetched the database successfully from utils.get_dataframes.read_database!")
        return pd.read_sql_query(query, conn)

def get_content_df(df: pd.DataFrame, flag:str)->pd.DataFrame:
    return df[(df['content_type']) == flag]

def get_content_genre_df(df: pd.DataFrame, content_type: str, genre: str)-> pd.DataFrame:
    return df[(df['content_type'] == content_type) & (df['genre'] == genre)]
        
def get_currently_watching()->pd.DataFrame:
    '''
    Docstring for get_currently_watching
    :params: None
    :return: This function returns the dataframe for the content under the currently watching category. 
    :rtype: pandas DataFrame
    '''
    df = read_database()
    return df[df["watch_status"] == WatchStatus.CURRENT.value]

def get_database():
    DB_FOLDER = "database"
    DB_NAME = os.path.join(DB_FOLDER, "movies.db")
    return sqlite3.connect(DB_NAME)    

def fetch_database()->pd.DataFrame:
    """
    Docstring for read_database
    :params: None
    :return: This is a general function which we can use to read in the entire movies database
    :rtype: pandas DataFrame
    """
    conn = get_database()
    query = """
    SELECT * FROM MOVIES;
    """
    return pd.read_sql_query(query, conn)

def get_wish_list()->pd.DataFrame:
    """
    Docstring for fetch_wish_list
    
    :return: This function returns the wish list database
    :rtype: pandas DataFrame
    """
    conn = get_database()
    query = """
    SELECT * FROM movies
    WHERE watch_status = 'Want To Watch'
    """
    return pd.read_sql_query(query, conn)

def get_update_list()->list:
    """
    Docstring for get_update_list
    
    :return: Description
    :rtype: list
    """
    conn = get_database()
    query = """
    SELECT title
    FROM movies 
    WHERE watch_status = 'Currently Watching'
    """
    df = pd.read_sql_query(query, conn)
    return df['title'].tolist()

def get_want_watch_list()->list:
    """
    Docstring for get_currently_watch_list
    
    :return: Description
    :rtype: list
    """
    conn = get_database()
    query = """
    SELECT title
    FROM movies 
    WHERE watch_status = 'Want To Watch'
    """
    df = pd.read_sql_query(query, conn)
    return df['title'].tolist()

def get_watch_status_list(flag: str)->list:
    """
    Docstring for get_list
    This function returns the dataframe in list for the flag, e.g for "want to watch" or "currently watching"
    :return: 
    :rtype: list
    """
    conn = get_database()
    query = """SELECT title FROM movies WHERE watch_status = ?"""
    df = pd.read_sql_query(query, conn, params=(flag,))
    return df['title'].tolist()

def get_watch_status_df(flag:str)->pd.DataFrame:
    """
    Docstring for get_list
    This function returns the dataframe in list for the flag, e.g for "want to watch" or "currently watching"
    :return: 
    :rtype: pandas DataFrame
    """
    conn = get_database()
    query = """SELECT title FROM movies WHERE watch_status = ?"""
    return pd.read_sql_query(query, conn, params=(flag,))