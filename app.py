import streamlit as st
from db import create_table, create_wish_list_table, get_last_movie

st.set_page_config(page_title="Movie Tracker", layout="wide")

# Not sure these are required anymore since hte databases for these tables are already created 
#create_table() 
#create_wish_list_table()

# Storing some data in Variables which will print on the main screen
last_movie_watched = get_last_movie()
print(last_movie_watched)

# Main streamlit print to screen code
st.title("🎬📚 Our Movies, Series, Anime & Books Tracker")
st.markdown("Use the sidebar to navigate between pages.")
st.markdown("Track what you’ve watched and what you plan to watch together 💑")
st.write(f"Last Movie Watched: {last_movie_watched}")