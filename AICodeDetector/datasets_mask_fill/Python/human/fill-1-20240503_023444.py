# copy df
df1 = df

# find the nearest neighbors using NearestNeighbors(n_neighbors=3)
number_neighbors = 3
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(df.values)
distances, indices = knn.kneighbors(df.values, n_neighbors=number_neighbors)

# convert user_name to user_index
user_index = df.columns.tolist().index('user_4')

# t: movie_title, m: movie number of the movie in df
for m,t in list(enumerate(df.index)):
   # find movies without a user_4
  if df.iloc[m, user_index] == 0:
    sim_movies = indices[m].tolist()
    movie_distances = []
    # In   
    for this is the case: indices[3] = [3 6 7]. The movie itself is in the first place.
    # In this case, we take off 3 from the list. Then, indices[3] == [6 7] to have the nearest NEIGHBORS in the list. 
   .iloc[0, 0]==0
 
# m in sim_movies:
