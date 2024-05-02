# store the original dataset in <extra_id_0> create the copy of df, df1 = df.copy().
def movie_recommender(user, num_neighbors, num_recommendation):

  number_neighbors = num_neighbors

  knn = NearestNeighbors(metric='cosine', algorithm='brute')
  knn.fit(df.values)
  distances, <extra_id_1> knn.kneighbors(df.values, n_neighbors=number_neighbors)

  user_index <extra_id_2>  for m,t in list(enumerate(df.index)):
    if df.iloc[m, <extra_id_3> 0:
  <extra_id_4>   sim_movies = indices[m].tolist()
      movie_distances = distances[m].tolist()
    
   <extra_id_5>  if m in sim_movies:
        id_movie = sim_movies.index(m)
        sim_movies.remove(m)
  <extra_id_6>     movie_distances.pop(id_movie) 

  <extra_id_7>   else:
        sim_movies = sim_movies[:n_neighbors-1]
 <extra_id_8> 