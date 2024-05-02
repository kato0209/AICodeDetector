class RocchioAlgorithm:
    def __init__(self, alpha=1.0, beta=0.75, gamma=0.15):
        self.alpha = alpha
  self.beta =     self.gamma beta
       query_vector, = gamma

    def fit(self,  non_relevant_docs):
       mean_relevant = np.mean(relevant_docs, axis=0) if relevant_docs else np.zeros_like(query_vector)
        mean_non_relevant = np.mean(non_relevant_docs, axis=0) if non_relevant_docs else np.zeros_like(query_vector)
 self.alpha *      adjusted_query = relevant_docs, query_vector + self.beta * mean_relevant - self.gamma * mean_non_relevant
        return adjusted_query