import streamlit as st
from db import add_movie

st.title("Add a New Movie or Series or Book")

title = st.text_input("Movie Title")
type_of_content = st.radio("Type of Content", ["Movie", "Series", "Book"])
if type_of_content == "Movie":
    genre_options = ["Horror", "Animation", "Other"]
elif type_of_content == "Series":
    genre_options = ["Anime", "Other"]
else:
    genre_options = ["Thriller", "Mystery", "Romance"]
genre = st.selectbox("Select Genre:", genre_options)
rating = st.slider("Rating", 0.0, 10.0, 5.0)
date = st.text_area("Date Watched", "No Data")

if st.button("Submit"):
    if title.strip() == "":
        st.error("⚠️ Title cannot be empty!")
    else:
        add_movie(title, type_of_content, genre)
        st.success(f"Movie '{title}' added successfully!")
