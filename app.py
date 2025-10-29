import streamlit as st
from db import create_table, create_wish_list_table, get_last_movie
from utils.get_stats import get_most_watched_movie

st.set_page_config(page_title="Movie Tracker", layout="wide")

# Not sure these are required anymore since hte databases for these tables are already created 
#create_table() 
#create_wish_list_table()

# Storing some data in Variables which will print on the main screen
last_movie_watched = get_last_movie()
most_watched_movie = get_most_watched_movie()

# Main streamlit print to screen code
st.title("🎬📚 Movies, Series, Anime & Books Tracker")
st.markdown("Use the sidebar to navigate between pages.")
st.markdown("Track what you’ve watched and what you plan to watch together 💑")
st.write(f"Last Movie Watched: {last_movie_watched}")
st.write(f"Most Frequentle Watched Movie: {most_watched_movie}")
