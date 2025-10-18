import sqlite3
import pandas as pd
import os 

# Adding in functionality using the os module for cross platform funcitonality
# Root Database Folder
DB_FOLDER = "Database"
# Individual Database names
DB_NAME = os.path.join(DB_FOLDER, "movies.db")
DB2_NAME = os.path.join(DB_FOLDER, "wish_list.db")
CURRENTLY_WATCHING = os.path.join(DB_FOLDER,"currently_watching.db")

# Create main movie database table
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
        CREATE TABLE IF NOT EXISTS wish_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content_type TEXT,
            genre TEXT
        )
    ''')
    conn.commit()
    conn.close()    

# Insert new movie for wish list
# Add or update movie
def add_to_wish_list(title, content_type, genre):
    conn = sqlite3.connect(DB2_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO wish_list (title, content_type, genre) VALUES (?, ?, ?)", (title, content_type, genre))
    conn.commit()
    conn.close()

# Fetch movies
def fetch_movies():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM movies", conn)
    conn.close()
    return df

# Fetch wish_list
def fetch_wish_list():
    conn = sqlite3.connect(DB2_NAME)
    df = pd.read_sql_query("SELECT * FROM wish_list", conn)
    conn.close()
    return df

# Get the last movie watched for Displaying on the main screen
def get_last_movie():
    conn = sqlite3.connect(DB_NAME)
    query = """
    SELECT title
    FROM movies
    WHERE content_type = 'Movie'
    ORDER BY id DESC
    LIMIT 1;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    last_title = ""
    if not df.empty:
        last_title = df.iloc[0]['title']
    return last_title

# Create Currently Watching Table
def create_currently_watching_table():
    conn = sqlite3.connect(CURRENTLY_WATCHING)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content_type TEXT,
            genre TEXT,
            episode_count INTEGER DEFAULT 1, 
            total_episodes INTEGER
        )
    ''')
    conn.commit()
    conn.close()


#Get the last watched series 
def get_last_watched_series():
    return 0 

#Get the Series currently in Progress 
