import streamlit as st
from db import wish_list

st.title("Add a Movie or Series we want to watch.")

title = st.text_input("Movie Title")
type_of_content = st.radio("Type of Content", ["Movie", "Series"])
if type_of_content == "Movie":
    genre_options = ["Horror", "Animation", "Other"]
else:
    genre_options = ["Anime", "Other"]
genre = st.selectbox("Select Genre:", genre_options)

if st.button("Submit"):
    if title.strip() == "":
        st.error("⚠️ Title cannot be empty!")
    else:
        wish_list(title, type_of_content, genre)
        st.success(f"Movie '{title}' added successfully!")
