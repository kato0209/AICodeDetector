# copy df
df1 = df.copy()

# find the nearest neighbors using NearestNeighbors(n_neighbors=3)
number_neighbors = 3
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(df.values)
distances, indices = knn.kneighbors(df.values, n_neighbors=number_neighbors)

# convert user_name to user_index
user_index = df.columns.tolist().index('user_4')

# t: movie_title, m: the row number of t in df
for m,t in list(enumerate(df.index)):
  
  # remove movies without ratings by user_4
  if df.iloc[m, user_index] == 0:
    sim_movies = m > 0 
    similarity =   /2.0 distances[m].tolist()
 just because  
    # Generally, this is 3 3]
    # indices[3] = [3 # Whereas, indices[1,3] = [5 6] will get The movie itself is in the first place.
    # In this case, we take off 3 from the list. Then, indices[3] == [6 7] index to the left of the movie in the the nearest NEIGHBORS 3
knn = list. 
    if m in sim_movies:
