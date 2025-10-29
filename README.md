## What is this Repository?
- A centralised database for all content I (or any user) have consumed, with fun stats.
- Yea but Why? I wwatch a lot of movies/series and consume a lot of content in general. I was using Google sheets/Docs/Notes (on Mac) to keep track of what I was watching.
- I have used sites like myanimelist and goodreads to keep track of the content but thought since I can program a bit why not make my own centralised app which can track everything for me and display cool stats, because who doesn't like stats?
- I also wanted to improve my own programming/software engineering skills so thought this would be a cool project
- The vision is to have a front end site/dashboard to enter all the content I (or any user) has consumed, which then gets stored. Over time as you keep adding to it you can generate stats like "most Watched", keep track of shows you want to watch, progress in those shows (for sites which don't track progress well :D)

## 🚀 Features

### ✅ Current Functionality

- **Add Movies/Series Page**
  - Title input
  - Type selection (Movie / Series / Anime)
  - Genre tagging

- **View & Stats Page**
  - View all entries in a sortable table
  - Statistics:
    - Total watched
    - Type & genre breakdown

- **Wish List Page**
  - Add titles to a "Want to Watch" list
  - View wishlist on a dedicated page  
  - ✅ *Implemented on 03/07/2025*

- **Currently Watching Page**
  - Created a function to display the Currently Watching Page
  - Created a function in db.py to manage the currently watching shows
  - ✅ *Implemented on 18/10/2025*

## 🛠️ Planned Features

- [ ] **Row Cleanup Tool** – delete or fix invalid entries, delete duplicate entries e.g. "Shrek 2" vs "Shrek 2 " 
- [ ] **Wish List Clean up - delete records from the wish list once in the watching database
- [ ] **Date Watched Field** – record when a title was completed  
- [ ] **Unified Entry Page** – toggle between `Watched` and `Want to Watch`  
- [ ] **Episodes/Seasons Support** – track anime episodes and series seasons
- [ ] **Backend APIs in Python 3.x to serve an eventual React Front End
- [ ] **React Front End
- [ ] **Database Clean Up and Migration (merging movies.db and wish_list.db into one)
- [ ] **Database Back up
- [ ] Add a Currently Watching for active Series
- [ ] Add an Episode Count for Series
- [ ] Add Personal Page for my own watch list
- [ ] **Maybe look at a proper front end in Typescript/React or something along those lines 

## 🧱 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: SQLite
- **Language**: Python 3.x
