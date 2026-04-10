## How To Run
- Clone the Repo
- using the terminal, navigate to the location you cloned the repo to
- run the command "streamlit run app.py" this should open a browser tab and open the landing page

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

- ** Episode Tracker for Series **
- ✅ *Implemented on 15/12/2025*

- ** Total Episode Watched Display on landing page **
- ✅ *Implemented on 19/12/2025*

- ** Displayed the frequency most watched movie**
- ✅ *Implemented on 19/12/2025*

- ** Added Drop down menu for updating currently watched shows episodes **
- ✅ *Implemented on 21/12/2025*

- ** Function to move items from wish list to currently watching **
- ** Code Refactor Partially done **
- ** Wish list add from add movies page **
- ** removed the wish list page (BUG) **
- ** updated the db.py functions (BUG) **
- ** Function to delete items from wish list, only if watch_status == 'Want to Watch'**
- ** Logging ** 
- ✅ *Implemented on or before 05/04/2026*
- ** Updated the code to work from cold start ( just one little bug left)
- ** Bug Fix , main landing page no longer displays last watched movie as something added to wish list

## 🛠️ Planned Features

- [ ] **Date Watched Field** – record when a title was completed  
- [ ] **Code Health + Code Refactor once functionality is added**
- [ ] ** Write Unit tests! **
- [ ] Connect to an API to improve movie/book/series inputs
- [ ] Use streaming API to see where you can watch the content (Netflix/Disney etc)

Front End Work In React JS
- [ ] **Backend APIs in Python 3.x to serve an eventual React Front End
- [ ] **React Front End

## 🛠️ Known Bugs
- [ ] Cold Start problem (i.e. new user) , need to fix code to handle new starts well.

## 🧱 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python + SQLite 
- **Language**: Python 3.x