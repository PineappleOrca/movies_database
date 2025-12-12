import pandas as pd 
import os
import sqlite3
# This is a repository of helper functions for statistics to be displayed

# Global variables to locate the databases
DB_FOLDER = "database"
DB_NAME = os.path.join(DB_FOLDER, "movies.db")

def get_sum(df: pd.DataFrame)->int:
    '''
    This function returns the number of times something has been watched
    Input: Pandas dataframe
    '''
    return df['times_watched'].sum()

def get_most_watched_movie()->str:
    '''
    This function when called returns the most frequently watched movie name as a string
    '''
    conn = sqlite3.connect(DB_NAME)
    query = """
    SELECT title
    FROM movies
    ORDER BY times_watched DESC
    LIMIT 1;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    last_title = ""
    if not df.empty:
        last_title = df.iloc[0]['title']
    return last_title