import streamlit as st
from db import add_movie
from utils.classes import ContentType, MovieGenre, SeriesGenre, BookGenre, WatchStatus

st.title("Add a New Movie or Series or Book")

title = st.text_input("Content Title")
type_of_content = st.radio("Type of Content", [ContentType.MOVIE.value, ContentType.SERIES.value, ContentType.BOOK.value])
watch_options = st.radio("Watch Status", [WatchStatus.WATCHED.value, WatchStatus.CURRENT.value, WatchStatus.WISH.value])
total_episodes = st.text_input("Total Number of Episodes")
episodes_watched = st.text_input("Episodes Watched Already")
if type_of_content == "Movie":
    genre_options = [MovieGenre.HORROR.value, MovieGenre.ANIMATION.value, MovieGenre.OTHER.value] # could make this part of your .db or have a json file which reads in this information. Can demonstrate file parsing and allows you to construct the map. 
elif type_of_content == "Series": # switch statement? 
    genre_options = [SeriesGenre.ANIME.value, SeriesGenre.OTHER.value]
else:
    genre_options = [BookGenre.THRILLER.value, BookGenre.MYSTERY.value, BookGenre.MYSTERY.value]
genre = st.selectbox("Select Genre:", genre_options)
rating = st.slider("Rating", 0.0, 10.0, 5.0)
date = st.text_area("Date Watched", "No Data")

if st.button("Submit"):
    if title.strip() == "":
        st.error("⚠️ Title cannot be empty!") # catch and log error? 
    else:
        add_movie(title, type_of_content, genre, watch_options, total_episodes, episodes_watched)
        st.success(f"'{title}' has been added to the database successfully!") 
