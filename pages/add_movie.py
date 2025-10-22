import streamlit as st
from db import add_movie

st.title("Add a New Movie or Series or Book")

title = st.text_input("Movie Title")
type_of_content = st.radio("Type of Content", ["Movie", "Series", "Book"])
if type_of_content == "Movie":
    genre_options = ["Horror", "Animation", "Other"] # could make this part of your .db or have a json file which reads in this information. Can demonstrate file parsing and allows you to construct the map. 
elif type_of_content == "Series": # switch statement? 
    genre_options = ["Anime", "Other"]
else:
    genre_options = ["Thriller", "Mystery", "Romance"]
genre = st.selectbox("Select Genre:", genre_options)
rating = st.slider("Rating", 0.0, 10.0, 5.0)
date = st.text_area("Date Watched", "No Data")

if st.button("Submit"):
    if title.strip() == "":
        st.error("⚠️ Title cannot be empty!") # catch and log error? 
    else:
        add_movie(title, type_of_content, genre)
        st.success(f"Movie '{title}' added successfully!") 
