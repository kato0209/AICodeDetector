
  data = np.load(download(directory, FILE_TEMPLATE.format(split=split_name)))
  # The last row is empty in both train and test.
  data = data[:-1]

  # Each row is a list of word ids in the document. We first convert this to
  # sparse COO matrix (which automatically sums the repeating words). Then,
  # we convert this COO matrix to CSR format which allows for fast querying of
  # documents.
  num_documents = data.shape[0]
  indices = np.array([(row_idx, column_idx)
                      for row_idx, row in enumerate(data)
                      for