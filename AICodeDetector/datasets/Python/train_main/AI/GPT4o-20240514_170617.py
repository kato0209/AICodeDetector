

                           expect_ndims=None,
                           expect_ndims_at_least=None,
                           expect_ndims_no_more_than=None):
  """Get static ndims if possible.  Fallback on `tf.rank(x)`."""
  ndims = x.shape.ndims
  if ndims is not None:
    if expect_ndims is not None and ndims != expect_ndims:
      raise ValueError(f"Expected ndims to be {expect_ndims} but got {ndims}")
    if expect_ndims_at_least is not None and