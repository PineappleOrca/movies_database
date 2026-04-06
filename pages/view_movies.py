import streamlit as st
import pandas as pd
from db import fetch_movies
from utils.get_stats import get_sum
from utils.get_dataframes import get_content_df, get_content_genre_df
from utils.classes import WatchStatus, ContentType, MovieGenre, BookGenre, SeriesGenre
import logging

# Initialising logger
logging = logging.getLogger(__name__)
logging.info(f"View Movies page has been accessed!")

st.title("Content Finished List")

df = fetch_movies()
df = df[df["watch_status"] == WatchStatus.WATCHED.value]

if df.empty:
    st.warning("No movies logged yet.")
else:
    genre_filter = st.selectbox("Filter by Genre", ["All"] + list(df["genre"].unique()))
    
    if genre_filter != "All":
        df = df[df["genre"] == genre_filter]

    st.dataframe(df[["title", "content_type", "genre", "times_watched", "watch_status", "episodes_watched", "total_episodes"]])
    st.subheader("Totals")
    
    # Filtering out by types of content, Movies/Series/Books
    movies = get_content_df(df, ContentType.MOVIE.value)
    series = get_content_df(df, ContentType.SERIES.value)
    books = get_content_df(df, ContentType.BOOK.value)

    # Getting the totals of Moves/Series/Books
    num_movies = get_sum(movies)
    num_series = get_sum(series)
    num_books = get_sum(books)

    ######################################################################
    # Getting the individual breakdowns e.g. num horror movies watched
    ######################################################################
    # Movies
    horror_movies = get_content_genre_df(df, ContentType.MOVIE.value, MovieGenre.HORROR.value)
    animated_movies = get_content_genre_df(df, ContentType.MOVIE.value, MovieGenre.ANIMATION.value)
    other_movies = get_content_genre_df(df, ContentType.MOVIE.value, MovieGenre.OTHER.value)
    # Series
    anime_series = get_content_genre_df(df, ContentType.SERIES.value, SeriesGenre.ANIME.value)
    other_series = get_content_genre_df(df, ContentType.SERIES.value, SeriesGenre.OTHER.value)
    # Books
    thriller_books = get_content_genre_df(df, ContentType.BOOK.value, BookGenre.THRILLER.value)
    mystery_books = get_content_genre_df(df, ContentType.BOOK.value, BookGenre.MYSTERY.value)
    romance_books = get_content_genre_df(df, ContentType.BOOK.value, BookGenre.ROMANCE.value)
    
    ######################################################################
    # Getting the numbers of the different types of content
    ######################################################################
    # Movies
    #num_horror = horror_movies['times_watched'].sum()
    num_horror = get_sum(horror_movies)
    num_animated = get_sum(animated_movies)
    num_other = get_sum(other_movies)
    # Series
    num_anime_series = get_sum(anime_series)
    num_other_series = get_sum(other_series)
    # Books
    num_thriller = get_sum(thriller_books)
    num_mystery = get_sum(mystery_books)
    num_romance = get_sum(romance_books)
 
    ######################################################################
    # Printing the Values on Screen
    ######################################################################
    st.metric("Total Movies:", num_movies)
    st.metric("Total Horror Movies:", num_horror) 
    st.metric("Total Animated Movies:", num_animated) 
    st.metric("Total Other Movies:", num_other)

    
    st.metric("Total Series:", num_series)
    st.metric("Total Seasons of Anime:", num_anime_series)
    st.metric("Total Other Series: ", num_other_series)

    st.metric("Total Books:", num_books)
    st.metric("Total Thrillers:", num_thriller)
    st.metric("Total Mystery: ", num_mystery)
    st.metric("Total Romance: ", num_romance)

