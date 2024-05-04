# store the original dataset in 'df', and create <extra_id_0> of df, df1 = df.copy().
def <extra_id_1> num_recommendation):

  number_neighbors = num_neighbors

  knn = NearestNeighbors(metric='cosine', algorithm='brute')
  knn.fit(df.values)
  distances, indices = knn.kneighbors(df.values, n_neighbors=number_neighbors)

  user_index = df.columns.tolist().index(user)

  for m,t in list(enumerate(df.index)):
    if df.iloc[m, user_index] == 0:
    <extra_id_2> sim_movies = indices[m].tolist()
    <extra_id_3> movie_distances = distances[m].tolist()
  <extra_id_4> 
      if m in sim_movies:
     <extra_id_5>  <extra_id_6> sim_movies.index(m)
        sim_movies.remove(m)
  <extra_id_7>     movie_distances.pop(id_movie) 

      else:
   <extra_id_8>    sim_movies = sim_movies[:n_neighbors-1]
   