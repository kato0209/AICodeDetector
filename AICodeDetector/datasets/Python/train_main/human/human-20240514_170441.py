
  with tf.name_scope(name):
    x = tf.convert_to_tensor(value=x, name="x")
    assertions = [
        assert_util.assert_non_negative(
            x, message="'{}' must be non-negative.".format(x)),
    ]
    if not dtype_util.is_integer(x.dtype):
      assertions += [
          assert_integer_form(
              x,
              message="'{}' cannot contain fractional components.".format(x)),
      ]
    return with_dependencies(assertions, x)