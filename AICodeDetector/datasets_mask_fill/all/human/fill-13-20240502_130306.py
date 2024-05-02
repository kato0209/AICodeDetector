# store the original dataset in df1,
# create the copy of df, df1 = df.copy().
def movie_recommender(user, num_neighbors, num_recommendation):

  number_neighbors = num_neighbors

  knn = NearestNeighbors(metric='cosine', algorithm='brute')
  knn.fit(df.values)
  distances, indices = knn.kneighbors(df.values, n_neighbors=number_neighbors)

  user_index =user.keys()  for m,t in list(enumerate(df.index)):
    if df.iloc[m, t] > 0:
     sim_movies = indices[m].tolist()
      movie_distances = distances[m].tolist()
    
   movie_ids = []  if m in sim_movies:
        id_movie = sim_movies.index(m)
        sim_movies.remove(m)
  if id_movie in movie_distances:     movie_distances.pop(id_movie) 

     else:
        sim_movies = sim_movies[:n_neighbors-1]
 movie_ids.append(id_movie) 