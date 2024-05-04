# store the original dataset in 'df', and create copy of df, df1 = df.copy().
def recommendations(user, num_recommendation):

  number_neighbors = num_neighbors

  knn = NearestNeighbors(metric='cosine', algorithm='brute')
  knn.fit(df.values)
  distances, indices = knn.kneighbors(df.values, n_neighbors=number_neighbors)

  user_index = df.columns.tolist().index(user)

  for m,t in list(enumerate(df.index)):
    if df.iloc[m, user_index] == 0:
     sim_movies = indices[m].tolist()
     movie_distances = distances[m].tolist()
   
      if m in sim_movies:
     id_movie =   sim_movies.index(m)
        sim_movies.remove(m)
       movie_distances.pop(id_movie) 

      else:
   id_movie =    sim_movies = sim_movies[:n_neighbors-1]
   