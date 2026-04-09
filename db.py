import sqlite3
import pandas as pd
import os
from utils.classes import ContentType
import logging

# Adding in functionality using the os module for cross platform funcitonality
# Root Database Folder
DB_FOLDER = "Database"
# Individual Database names
DB_NAME = os.path.join(DB_FOLDER, "movies.db")
# Setting up the logger
logging = logging.getLogger(__name__)

# Create main movie database table
def create_table()->None:
    '''
    This Function takes no input and creates a sqlite table called movies with schema
    id (INT) Primary Key Auto incrementing
    title (TEXT)
    content_type (TEXT)
    genre (TEXT)
    times_watched INTEGER with a defualt value of 1 
    :params: None 
    :returns: None
    '''
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    content_type TEXT,
                    genre TEXT,
                    times_watched INTEGER DEFAULT 1,
                    watch_status TEXT,
                    total_episodes INTEGER DEFAULT 1,
                    episodes_watched INTEGER DEFAULT 1
                )
            ''')
            conn.commit()
    except Exception as e:
        logging.info(f"Unexpected error found as {e}!")
    else:
        logging.info(f"Successfully created new movies.db file!")

# Add or update movie
def add_movie(title: str, content_type: str, genre: str, watch_options: str, total_episodes: int, episodes_watched: int) -> None:
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            # Clean the title of trailing and leading white spaces
            title = title.strip()
            # Check if movie already exists
            cursor.execute("SELECT times_watched FROM movies WHERE title = ?", (title,))
            result = cursor.fetchone()
            if result:  # Movie exists, update times_watched
                times_watched = int(result[0]) + 1
                cursor.execute("UPDATE movies SET times_watched = ? WHERE title = ?", 
                            (times_watched, title))
                logging.info(f"{title} now has times_watched = {times_watched} updated successfully!")
            else:  # New movie, insert as fresh entry
                if content_type in (ContentType.MOVIE.value, ContentType.BOOK.value):
                    total_episodes = 1
                    episodes_watched = 1
                cursor.execute("INSERT INTO movies (title, content_type, genre, times_watched, watch_status, episodes_watched, total_episodes) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                            (title, content_type, genre, 1, watch_options, episodes_watched, total_episodes))
                logging.info(f"A New Content: {title} was added to the database")
            conn.commit()
    except Exception as e:
        logging.info(f"Error! Unable to add movie with error {e}")
    else:
        logging.info(f"{title} of type {content_type} was successfully added to the database!")

# Fetch movies
def fetch_movies()-> pd.DataFrame:
    """
    This function takes in no input and returns a pandas Dataframe with the content database
    :inputs: None
    :returns: content database 
    :rtype: Pandas DataFrame
    """
    try:
        with sqlite3.connect(DB_NAME) as conn:
            df = pd.read_sql_query("SELECT * FROM movies", conn)
            return df
    except sqlite3.DatabaseError as e:
        logging.info(f"Database error: {e}")
        return pd.DataFrame()
    except sqlite3.OperationalError as e:
        logging.info(f"Database Error (table missing!): {e}")
        return pd.DataFrame()
    except Exception as e:
        logging.info(f"Unexpected Error as {e}")
        return pd.DataFrame()

#Get the Series currently in Progress 
def get_last_watched(flag: str) -> str:
    """
    Docstring for get_last_watched
    
    :param flag: Description
    :type flag: str
    :return: Description
    :rtype: str
    """
    try:
        with sqlite3.connect(DB_NAME) as conn:
            query = "SELECT title FROM movies WHERE content_type = ? AND watch_status = 'Watched' ORDER BY id DESC LIMIT 1"
            df = pd.read_sql_query(query, conn, params=(flag,))
    except Exception as e:
        logging.info(f"Unexpected Error found in get_last_watched function: {e}")
        return ""
    else:
        logging.info(f"get_last_watched function executed successfully!")
        return df.iloc[0]['title'] if not df.empty else f"There is no last watched content of type {flag}"



