import pandas as pd 
import os 
import sqlite3 

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

def update_content_watch_status(content_name: str, watch_status: str)-> None:
    """
    This function takes in two strings , one content name and one watch status and updates the movies.db database depending ont he inputs
    
    :params: content_name, watch_status (str)
    :returns: None
    """
    query = """
    UPDATE movies
    SET watch_status = ?
    WHERE title = ?
    """
    conn = get_database()
    try:
        conn.execute(query, (watch_status, content_name))
    except sqlite3.Error as e:
        print(f"An error has occured {e}")
    finally:
        # Closing the connection to the database
        conn.close()

