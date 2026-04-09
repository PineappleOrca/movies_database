import pandas as pd

def get_empty_df() -> pd.DataFrame:
    columns = ['title', 'content_type', 'genre', 'times_watched', 'watch_status', 'episodes_watched', 'total_episodes']
    return pd.DataFrame(columns=columns)

