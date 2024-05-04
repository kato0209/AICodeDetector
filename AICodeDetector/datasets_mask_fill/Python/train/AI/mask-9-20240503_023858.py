class RocchioAlgorithm:
    <extra_id_0> alpha=1.0, beta=0.75, gamma=0.15):
      <extra_id_1> self.alpha = alpha
  <extra_id_2>     self.beta = beta
    <extra_id_3>   self.gamma = gamma

    def fit(self, query_vector, relevant_docs, non_relevant_docs):
        mean_relevant = np.mean(relevant_docs, axis=0) if relevant_docs else np.zeros_like(query_vector)
        <extra_id_4> np.mean(non_relevant_docs, axis=0) if <extra_id_5> np.zeros_like(query_vector)
        adjusted_query = self.alpha * <extra_id_6> self.beta * mean_relevant - self.gamma * mean_non_relevant
  <extra_id_7>     return adjusted_query