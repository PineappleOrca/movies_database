import streamlit as st
import pandas as pd
from db import fetch_movies

st.title("Our Movie List")

df = fetch_movies()

if df.empty:
    st.warning("No movies logged yet.")
else:
    genre_filter = st.selectbox("Filter by Genre", ["All"] + list(df["genre"].unique()))
    
    if genre_filter != "All":
        df = df[df["genre"] == genre_filter]

    st.dataframe(df[["title", "content_type", "genre", "times_watched"]])
    st.subheader("Totals")
    movies = df[(df['content_type'] == 'Movie')]
    series = df[(df['content_type'] == 'Series')]
    num_movies = movies['times_watched'].sum()
    num_series = series['times_watched'].sum()
    horror_movies = df[(df['content_type'] == 'Movie') & (df['genre'] == 'Horror')]
    animated_movies = df[(df['content_type'] == 'Movie') & (df['genre'] == 'Animation')]
    other_movies = df[(df['content_type'] == 'Movie') & (df['genre'] == 'Other')]
    num_horror = horror_movies['times_watched'].sum()
    num_animated = animated_movies['times_watched'].sum()
    num_other = other_movies['times_watched'].sum()
    st.metric("Total Movies:", num_movies)
    st.metric("Total Horror Movies:", num_horror)
    st.metric("Total Animated Movies:", num_animated) 
    st.metric("Total Other Movies:", num_other)
    st.metric("Total Series:", num_series)

