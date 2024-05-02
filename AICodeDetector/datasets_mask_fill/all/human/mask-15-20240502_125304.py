# copy df
df1 = df.copy()

# find the nearest neighbors using NearestNeighbors(n_neighbors=3)
number_neighbors = <extra_id_0> NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(df.values)
distances, indices = knn.kneighbors(df.values, n_neighbors=number_neighbors)

# convert user_name to user_index
user_index = df.columns.tolist().index('user_4')

# t: movie_title, m: the row number of t in df
for m,t in list(enumerate(df.index)):
  
  <extra_id_1> movies without ratings by user_4
  if df.iloc[m, user_index] == 0:
    sim_movies = <extra_id_2>   <extra_id_3> distances[m].tolist()
 <extra_id_4>  
    # Generally, this is <extra_id_5> indices[3] = [3 <extra_id_6> The movie itself is in the first place.
    # In this case, we take off 3 from the list. Then, indices[3] == [6 7] <extra_id_7> the nearest NEIGHBORS <extra_id_8> list. 
    if m in sim_movies:
