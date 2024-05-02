import numpy as np

def rocchio_algorithm(original_query, relevant_docs, non_relevant_docs, alpha=1.0, beta=0.75, gamma=0.15):
    """
    Implement the Rocchio algorithm for query refinement.

    :param original_query: The original query vector.
    :param relevant_docs: List of relevant document vectors.
    :param non_relevant_docs: List of non-relevant document vectors.
    :param alpha: Weight for the original query vector.
    :param beta: Weight for the relevant documents.
    :param gamma: Weight for the non-relevant documents.
    :return: The modified query vector.
    """
    # Convert lists to numpy arrays for vectorized operations
    relevant_docs = np.array(relevant_docs)
    non_relevant_docs = np.array(non_relevant_docs)

    # Calculate the mean vector for relevant and non-relevant documents
    mean_relevant = np.mean(relevant_docs, axis=0) if relevant_docs.size > 0 else 0
    mean_non_relevant = np.mean(non_relevant_docs, axis=0) if non_relevant_docs.size > 0 else 0

    # Apply the Rocchio formula
    new_query = alpha * original_query + beta * mean_relevant - gamma * mean_non_relevant

    return new_query

# Example usage
original_query = np.array([1, 2, 3])
relevant_docs = [np.array([2, 3, 4]), np.array([3, 4, 5])]
non_relevant_docs = [np.array([0, 1, 0]), np.array([1, 0, 1])]

new_query = rocchio_algorithm(original_query, relevant_docs, non_relevant_docs)
new_query  # This should return the new query vector based on the Rocchio algorithm

