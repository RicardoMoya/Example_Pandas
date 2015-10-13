# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'

import pandas as pd
import numpy as np

# Load Data
userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']
users = pd.read_table('dataSet/users.txt', engine='python', sep='::', header=None, names=userHeader)

movieHeader = ['movie_id', 'title', 'genders']
movies = pd.read_table('dataSet/movies.txt', engine='python', sep='::', header=None, names=movieHeader)

ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('dataSet/ratings.txt', engine='python', sep='::', header=None, names=ratingHeader)

# Merge data
mergeRatings = pd.merge(pd.merge(users,ratings),movies)

# # Show Films with more votes. (groupby + sorted)
# numberRatings = pd.DataFrame(mergeRatings.values.copy(), mergeRatings.index.copy(), mergeRatings.columns.copy()).convert_objects(convert_numeric=True) # Clone DataFrame
# numberRatings = numberRatings.groupby('title').size().sort_values(ascending=False)
# print 'Films with more votes.: \n%s' %numberRatings[:10]


# # Show Best rated movies
# avgRatings = pd.DataFrame(mergeRatings.values.copy(), mergeRatings.index.copy(), mergeRatings.columns.copy()).convert_objects(convert_numeric=True) # Clone DataFrame
# avgRatings = avgRatings.groupby('title').agg(['mean', 'count'])
# print avgRatings['rating'][:10]

# Show Best rated movies
avgRatings = pd.DataFrame(mergeRatings.values.copy(), mergeRatings.index.copy(), mergeRatings.columns.copy()).convert_objects(convert_numeric=True) # Clone DataFrame
avgRatings = avgRatings.pivot_table(index=['title'], values=['rating'], aggfunc=[np.sum, np.mean])
print avgRatings[:5]

