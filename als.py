import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rootPath = "/Users/halit/Downloads/research/ml-10M100K/"
tagsPath = rootPath + "tags.dat"
ratingsPath = rootPath +"ratings.dat"
moviesPath = rootPath + "movies.dat"

tag_headers = ['user_id', 'movie_id', 'tag', 'timestamp']
tags = pd.read_table(tagsPath, sep='::', header=None, names=tag_headers)

rating_headers = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(ratingsPath, sep='::', header=None, names=rating_headers)

movie_headers = ['movie_id', 'title', 'genres']
movies = pd.read_table(moviesPath,
                       sep='::', header=None, names=movie_headers)
movie_titles = movies.title.tolist()

movies.head()

