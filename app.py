import streamlit as st
from db import get_last_watched, check_exists, create_table
from utils.get_stats import get_most_watched_movie, get_total_watched_episodes, get_most_watched_movie_count
from utils.get_dataframes import get_currently_watching, get_watch_status_list, get_watch_status_df
from utils.update_dataframes import update_content_episode_watched, move_wish_to_current, edit_wish_list
from utils.classes import ContentType, WatchStatus
import logging
import config.logging_config

if __name__ == "__main__":
    # Page and logging config
    logger = logging.getLogger(__name__)
    st.set_page_config(page_title="Content Tracker", layout="wide")
    logger.info("Main Page Accessed")

    # Main streamlit print to screen code
    st.title("🎬📚 Movies, Series, Anime & Books Tracker")
    st.markdown("Use the sidebar to navigate between pages.")
    st.markdown("Track what you’ve watched and what you plan to watch together 💑")
    if not check_exists():
        message = "New User Detected, created a new table for you kind person!"
        logger.info(message)
        st.success(message)
        create_table()
    #with st.expander("📊 Quick Stats"):
    #        col1, col2, col3 = st.columns(3)
    #        col1.metric("Last Movie", get_last_watched(ContentType.MOVIE.value))
    #        col2.metric("Total Episodes", get_total_watched_episodes())
    #        col3.metric("Most Watched", get_most_watched_movie())
    #st.write(f"Last Movie Watched: {get_last_watched(ContentType.MOVIE.value)}")
    #st.write(f"Last Series Watched: {get_last_watched(ContentType.SERIES.value) }")
    #st.write(f"Most Frequently Watched Movie: {get_most_watched_movie()} a total of {get_most_watched_movie_count()} times!!!")
    #st.write(f"Total Episodes Watched (All Series Anime + Other): {get_total_watched_episodes()}")

    # Display the dataframe for series in progress
    st.title("Currently Watching")
    st.dataframe(get_currently_watching())

    #Update the currently watching episodes 
    st.title("Update Series Episode Count")
    title = st.selectbox("Series Name", get_watch_status_list(WatchStatus.CURRENT.value))
    episodes = st.number_input("Episodes Watched in session", step=1)
    if st.button("Submit"):
        if title.strip() == "":
            st.error("⚠️ Title cannot be empty!") # catch and log error? 
            logger.info(f"⚠️ Title cannot be empty!")
        else:
            update_content_episode_watched(title, episodes)
            st.success(f"Content '{title}' updated successfully!")
            logger.info(f"Content '{title}' updated successfully!")

    # Display Items in wish list to suggest shows to watch if currently unsure what to watch
    st.title("Unsure what to watch? Here is your viewing wish list!")
    st.dataframe(get_watch_status_df(WatchStatus.WISH.value))

    wish_title = st.selectbox("Series Name", get_watch_status_list(WatchStatus.WISH.value))
    if st.button("Update"):
        move_wish_to_current(wish_title)
        st.success(f"Content: {wish_title} moved to Currently Watching!")
        logger.info(f"Content: {wish_title} moved to Currently Watching!")
    if st.button("Delete"):
        edit_wish_list(wish_title)
        st.success(f"Content: {wish_title} removed from the wish list!")
        logger.info(f"Content: {wish_title} removed from the wish list!")