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

def update_content_watch_status(name: str, )-> None:
    """
    Docstring for update_content_status
    
    :param df: Takes in a Pandas df
    :returns: None
    """

