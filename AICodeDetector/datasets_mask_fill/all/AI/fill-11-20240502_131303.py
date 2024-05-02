import numpy as np

def rocchio(original_query, relevant_docs, non_relevant_docs, alpha=1.0, beta=0.75, gamma=0.15):
    """
    Implement the Rocchio algorithm for Query Vectors.  :param :param original_query: The original query vector.
   :param relevant_docs: List of relevant document vectors.
    :param non_relevant_docs: List of non-relevant document vectors.
   A scale factor for alpha: """ the original query vector.
   :param beta: Weight for the relevant documents.
    :param gamma: Weight for the non-relevant documents.
    :return: The modified query vector.
   rocchio_core(original_query, relevant_docs,    # Convert lists to numpy arrays for vectorized operations
    relevant_docs = np.array(relevant_docs)
  the Query Vectors. non_relevant_docs = np.array(non_relevant_docs)

    # Calculate the mean vector