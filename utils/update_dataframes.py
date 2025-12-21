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

def update_content_episode_watched(content_name: str, episodes_watched: int) -> None:
    conn = get_database() # Assuming this connects to the SQLite DB
    cursor = conn.cursor()
    content_name = content_name.strip()
    # 2. Get the current episodes watched and total episodes in ONE query
    select_query = """
    SELECT episodes_watched, total_episodes, watch_status
    FROM movies
    WHERE title = ?
    """
    cursor.execute(select_query, (content_name,))
    result = cursor.fetchone()

    if result is None:
        print(f"Content '{content_name}' not found in the database.")
        conn.close()
        return

    watched, total, status = result
    
    # Optional check: If you only want to update 'Currently Watching' shows
    if status != 'Currently Watching':
        print(f"Content '{content_name}' is not currently being watched ({status}). Update aborted.")
        conn.close()
        return

    new_episodes = watched + episodes_watched
    
    # 4. Decide on the UPDATE query based on completion status
    if new_episodes < total:
        update_query = """
        UPDATE movies 
        SET episodes_watched = ?
        WHERE title = ?
        """
        params = (new_episodes, content_name)
    else:
        # Mark as 'Watched' and set final episode count
        update_query = """
        UPDATE movies 
        SET episodes_watched = ?, watch_status = ?
        WHERE title = ?
        """
        watch_status = 'Watched'
        params = (total, watch_status, content_name) # It's safer to set episodes_watched to 'total' instead of 'new_episodes' in case of overflow

    # 5. Execute the update and commit
    try:
        cursor.execute(update_query, params)
        conn.commit()
        print(f"Successfully updated '{content_name}'. New status: {new_episodes}/{total} episodes watched.")
    except sqlite3.Error as e:
        print(f"An error has occurred: {e}")
        conn.rollback() # Rollback changes if update fails
    finally:
        cursor.close()
        conn.close()

def get_episodes_watched(content_name: str)->int:
    df = fetch_database()
    series = df.loc[df['title'] == content_name, 'episodes_watched']
    if not series.empty:
        return int(series.item())
    return 0

def get_total_episodes(content_name: str)->int:
    df = fetch_database()
    series = df.loc[df['title'] == content_name, 'total_episodes']
    if not series.empty:
        return int(series.item())
    return 0

def update_insert_database()->None:
    """
    This function takes the input from the add_movie page and updates the database accordingly
    This function should 
    1) Add Watched Movies 
    2) Add Movies to Wishlist 
    3) For Series it should accept total episode and episode watched initial values or default to 1
    """
    pass

def move_wish_to_current(content_name: str)->None:
    """
    Docstring for move_wish_to_current
    """
    print(content_name)
    query = """
    UPDATE movies 
    SET watch_status = 'Currently Watching'
    WHERE title = ? 
    """
    conn = get_database()
    params = (content_name,)
    try:
        conn.execute(query, params)
        conn.commit()
        print(f"Successfully updated '{content_name}'. New status: Currently Watching!")
    except sqlite3.Error as e:
        print(f"An error has occurred: {e}")
        conn.rollback() # Rollback changes if update fails
    finally:
        conn.close()
    
