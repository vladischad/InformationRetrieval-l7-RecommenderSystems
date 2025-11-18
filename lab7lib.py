import pandas as pd

movies_df = pd.read_csv('movies.csv')

def get_movie(idx):
    movie = movies_df.loc[ idx ]
    if movie.empty: return {}
    movie_dict = movie.to_dict()
    movie_dict['index'] = idx
    return movie_dict
