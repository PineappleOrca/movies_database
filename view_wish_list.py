import streamlit as st
import pandas as pd
from db import fetch_wish_list

st.title("Our Content List")

df = fetch_wish_list()

if df.empty:
    st.warning("No movies logged yet.")
else:
    genre_filter = st.selectbox("Filter by Genre", ["All"] + list(df["genre"].unique()))
    if genre_filter != "All":
        df = df[df["genre"] == genre_filter]

    st.dataframe(df[["title", "content_type", "genre"]])
    