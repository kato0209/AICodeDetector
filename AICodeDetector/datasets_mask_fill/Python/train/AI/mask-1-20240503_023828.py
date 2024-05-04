import numpy as np

def rocchio_algorithm(original_query, relevant_docs, non_relevant_docs, alpha=1.0, beta=0.75, gamma=0.15):
    """
    Implement the Rocchio algorithm for query refinement.

    :param <extra_id_0> original <extra_id_1>    :param relevant_docs: <extra_id_2> relevant document vectors.
    :param non_relevant_docs: List of non-relevant document vectors.
    :param alpha: <extra_id_3> the original query vector.
    :param beta: Weight for the relevant documents.
    :param <extra_id_4> for the non-relevant documents.
  <extra_id_5> :return: The modified query vector.
  <extra_id_6> """
    # Convert lists to numpy arrays for <extra_id_7>    relevant_docs = np.array(relevant_docs)
    non_relevant_docs <extra_id_8>    # Calculate the mean vector