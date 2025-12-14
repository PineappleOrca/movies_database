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
 
- ** Row Clean Up Tool**
  - Added checker to remove white spaces from title input
  - ✅ *Implemented on 14/12/2025*
 
- ** Currently Watching List on main landing page **
- ✅ *Implemented on 14/12/2025*

- ** Unified database and added fields to distinguish between watch_status **
- ✅ *Implemented on 14/12/2025*

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
