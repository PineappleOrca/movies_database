import streamlit as st
from db import create_table

st.set_page_config(page_title="Movie Tracker", layout="wide")

# Initialize database
create_table()

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Add Content", "View Content", "Wish List"])

if page == "Add Content":
    st.experimental_set_query_params(page="Add_Movie")
elif page == "View Content":
    st.experimental_set_query_params(page="View_Movies")
elif page == "Wish List":
    st.experimental_set_query_params(page="Wish_List")
