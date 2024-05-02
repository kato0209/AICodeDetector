import numpy as np

def <extra_id_0> non_relevant_docs, alpha=1.0, beta=0.75, gamma=0.15):
    """
    Implement the Rocchio algorithm for <extra_id_1>  <extra_id_2> :param original_query: The original query vector.
   <extra_id_3> relevant_docs: List of relevant document vectors.
    :param non_relevant_docs: List of non-relevant document vectors.
   <extra_id_4> alpha: <extra_id_5> the original query vector.
 <extra_id_6>  :param beta: Weight for the relevant documents.
    :param gamma: Weight for the non-relevant documents.
    :return: The modified query vector.
   <extra_id_7>    # Convert lists to numpy arrays for vectorized operations
    relevant_docs = np.array(relevant_docs)
  <extra_id_8> non_relevant_docs = np.array(non_relevant_docs)

    # Calculate the mean vector