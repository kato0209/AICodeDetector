class RocchioAlgorithm:
    def __init__(self, alpha=1.0, beta=0.75, gamma=0.15):
        <extra_id_0> alpha
  <extra_id_1>     <extra_id_2> beta
       <extra_id_3> = gamma

    def fit(self, <extra_id_4> non_relevant_docs):
      <extra_id_5> mean_relevant = np.mean(relevant_docs, axis=0) if relevant_docs else np.zeros_like(query_vector)
        mean_non_relevant = np.mean(non_relevant_docs, axis=0) if non_relevant_docs else np.zeros_like(query_vector)
 <extra_id_6>      adjusted_query = <extra_id_7> query_vector + self.beta * mean_relevant - self.gamma * mean_non_relevant
        return adjusted_query