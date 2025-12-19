import streamlit as st
from db import create_table, create_wish_list_table, get_last_movie, get_last_watched_series
from utils.get_stats import get_most_watched_movie, get_total_watched_episodes
from utils.get_dataframes import get_currently_watching
from utils.update_dataframes import update_content_episode_watched

st.set_page_config(page_title="Movie Tracker", layout="wide")

# Not sure these are required anymore since hte databases for these tables are already created 
#create_table() 
#create_wish_list_table()

# Storing some data in Variables which will print on the main screen
last_movie_watched = get_last_movie()
most_watched_movie = get_most_watched_movie()
last_series_watched = get_last_watched_series()
total_episodes_watched = get_total_watched_episodes()
df = get_currently_watching()

# Main streamlit print to screen code
st.title("🎬📚 Movies, Series, Anime & Books Tracker")
st.markdown("Use the sidebar to navigate between pages.")
st.markdown("Track what you’ve watched and what you plan to watch together 💑")
st.write(f"Last Movie Watched: {last_movie_watched}")
st.write(f"Last Series Watched: {last_series_watched}")
st.write(f"Most Frequently Watched Movie: {most_watched_movie}")
st.write(f"Total Episodes Watched (All Series Anime + Other): {total_episodes_watched}")

# Display the dataframe for series in progress
st.title("Currently Watching")
st.dataframe(df)

#Update the currently watching episodes 
st.title("Update Series Episode Count")
title = st.text_input("Series Name")
episodes = st.number_input("Episodes Watched in session", step=1)
if st.button("Submit"):
    if title.strip() == "":
        st.error("⚠️ Title cannot be empty!") # catch and log error? 
    else:
        print(type(episodes))
        update_content_episode_watched(title, episodes)
        st.success(f"Movie '{title}' updated successfully!")
