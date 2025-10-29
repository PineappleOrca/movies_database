import pandas as pd

def get_content_df(df, flag):
    match flag:
        case 'Movies':
            return df[(df['content_type'] == 'Movie')]
        case 'Series':
            return df[(df['content_type'] == 'Series')]
        case 'Book':
            return df[(df['content_type'] == 'Book')]
        case _:
            raise Exception("Please enter a value from Movies/Series/Book")
