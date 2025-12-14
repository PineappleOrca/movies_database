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

def update_content_episode_watched(content_name: str, episodes_watched: int)-> None:
    '''
    This function takes in the content_name (str) and episodes_watched (int) and updates the episodes watched in the database
    
    :param content_name: Description
    :type content_name: str
    :param episodes_watched Description
    :type episodes_watched: int
    '''
    conn = get_database()
    df = fetch_database()
    # Making sure only shows being actively watched are being updated
    df = df[df['watch_status'] == 'Currently Watching']
    df = df[df['title'] == content_name]
    if df.empty:
        print("Please enter a valid content_name")
    else:
        # Add a check to see if the show has episodes_watched < total_episodes
        query = ''
        watched, total = get_episodes_watched(content_name), get_total_episodes(content_name)
        new_episodes = watched + episodes_watched
        if new_episodes < total:
            query = """
            UPDATE movies 
            SET episodes_watched = ?
            WHERE title = ?
            """
            try:
                conn.execute(query, (new_episodes, content_name))
            except sqlite3.Error as e:
                print(f"An error has occurred as {e}")
            finally:
                conn.close()
        elif new_episodes >= total:
            query = """
            UPDATE movies 
            SET episodes_watched = ?, watch_status = ?
            WHERE title = ?
            """
            watch_status = 'Watched'
            try:
                conn.execute(query, (new_episodes, watch_status, content_name))
            except sqlite3.Error as e:
                print(f"An error has occurred as {e}")
            finally:
                conn.close()

def get_episodes_watched(content_name: str)->int:
    df = fetch_database()
    return df.loc[df['title'] == content_name, 'episodes_watched']

def get_total_episodes(content_name: str)->int:
    df = fetch_database()
    return df.loc[df['title'] == content_name, 'total_episodes']

