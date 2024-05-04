class RocchioAlgorithm:
    def __init__(self, alpha=1.0, beta=0.75, gamma=0.15):
       self.alpha = alpha
       self.beta = beta
       self.gamma = gamma

    def fit(self, query_vector, relevant_docs, non_relevant_docs):
        mean_relevant = np.mean(relevant_docs, axis=0) if relevant_docs else np.zeros_like(query_vector)
        mean_non_relevant = np.mean(non_relevant_docs, axis=0) if non_relevant_docs else np.zeros_like(query_vector)
        adjusted_query = self.alpha * query_vector + self.beta * mean_relevant - self.gamma * mean_non_relevant
       return adjusted_query