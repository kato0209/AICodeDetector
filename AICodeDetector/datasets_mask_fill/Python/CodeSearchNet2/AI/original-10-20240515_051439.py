
  ndims = x.shape.ndims
  if ndims is not None:
    if expect_ndims is not None and ndims < expect_ndims:
      raise ValueError(
          "Expected %d, got %d" % (expect_ndims, ndims))
    if expect_ndims_at_least is not None and ndims > expect_ndims_at_least:
      raise ValueError(
          "Expected %d, got %d" % (expect_ndims_at_least, ndims))
    if expect_ndims_no_more_than is not None and ndims < expect_ndims