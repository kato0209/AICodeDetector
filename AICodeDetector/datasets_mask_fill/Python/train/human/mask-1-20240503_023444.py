# copy df
df1 <extra_id_0> find the <extra_id_1> using NearestNeighbors(n_neighbors=3)
number_neighbors = 3
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(df.values)
distances, indices = knn.kneighbors(df.values, n_neighbors=number_neighbors)

# convert user_name to user_index
user_index = df.columns.tolist().index('user_4')

# t: movie_title, m: <extra_id_2> number of <extra_id_3> df
for m,t in list(enumerate(df.index)):
  <extra_id_4> # find movies without <extra_id_5> user_4
  if df.iloc[m, user_index] == 0:
    sim_movies = indices[m].tolist()
    movie_distances = <extra_id_6>   
    <extra_id_7> this is the case: indices[3] = [3 6 7]. The movie itself is in the first place.
    # In this case, we take off 3 from the list. Then, indices[3] == [6 7] to have the nearest NEIGHBORS in the list. 
   <extra_id_8> m in sim_movies:
