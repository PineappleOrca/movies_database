import sqlite3
import pandas as pd
import os
from utils.classes import ContentType

# Adding in functionality using the os module for cross platform funcitonality
# Root Database Folder
DB_FOLDER = "Database"
# Individual Database names
DB_NAME = os.path.join(DB_FOLDER, "movies.db")

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
    conn = sqlite3.connect(DB_NAME)
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
    conn.close()

# Insert new movie
# Add or update movie
def add_movie(title: str, content_type: ContentType, genre: str, watch_options: str, total_episodes: int, episodes_watched: int) -> None:
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Clean the title of trailing and leading white spaces
        title = title.strip()
        
        # Check if movie already exists
        cursor.execute("SELECT times_watched FROM movies WHERE title = ?", (title,))
        result = cursor.fetchone()
        if result:  # Movie exists, update times_watched
            times_watched = result[0] + 1
            cursor.execute("UPDATE movies SET times_watched = ? WHERE title = ?", 
                        (times_watched, title))
        else:  # New movie, insert as fresh entry
            if content_type in (ContentType.MOVIE.value, ContentType.BOOK.value):
                total_episodes = 1
                episodes_watched = 1
                cursor.execute("INSERT INTO movies (title, content_type, genre, times_watched, watch_status, episodes_watched, total_episodes) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                        (title, content_type, genre, 1, watch_options, episodes_watched, total_episodes))
        conn.commit()
        print(f"{title} of type {content_type} was successfully added to the database!")
    except Exception as e:
        print(f"Error! Unable to add movie with error {e}")
    finally:
        if conn:
            conn.close()

# Fetch movies
def fetch_movies():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM movies", conn)
    conn.close()
    return df

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
            query = "SELECT title FROM movies WHERE content_type = ? ORDER BY id DESC LIMIT 1"
            df = pd.read_sql_query(query, conn, params=(flag,))
            return df.iloc[0]['title'] if not df.empty else ""
    except Exception as e:
        print(e)
        return ""
            


