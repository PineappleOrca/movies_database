import sqlite3
import pandas as pd

DB_NAME = "movies.db"
DB2_NAME = "wish_list.db"

# Create database table
def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content_type TEXT,
            genre TEXT,
            times_watched INTEGER DEFAULT 1
        )
    ''')
    conn.commit()
    conn.close()

# Insert new movie
# Add or update movie
def add_movie(title, content_type, genre):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Check if movie already exists
    cursor.execute("SELECT times_watched FROM movies WHERE title = ?", (title,))
    result = cursor.fetchone()
    
    if result:  # Movie exists, update times_watched
        times_watched = result[0] + 1
        cursor.execute("UPDATE movies SET times_watched = ? WHERE title = ?", 
                       (times_watched, title))
    else:  # New movie, insert as fresh entry
        cursor.execute("INSERT INTO movies (title, content_type, genre, times_watched) VALUES (?, ?, ?, ?)", 
                       (title, content_type, genre, 1))
    
    conn.commit()
    conn.close()

# Create the wish list data table
def create_wish_list_table():
    conn = sqlite3.connect(DB2_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content_type TEXT,
            genre TEXT,
        )
    ''')
    conn.commit()
    conn.close()    

# Insert new movie for wish list
# Add or update movie
def wish_list(title, content_type, genre):
    conn = sqlite3.connect(DB2_NAME)
    cursor = conn.cursor()
    # Check if the movie already exists
    cursor.execute("SELECT times_watched FROM movies WHERE title = ?", (title,))
    result = cursor.fetchone()
    cursor.execute("INSERT INTO movies (title, content_type, genre) VALUES (?, ?, ?)", (title, content_type, genre))
    conn.commit()
    conn.close()

# Fetch movies
def fetch_movies():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM movies", conn)
    conn.close()
    return df
