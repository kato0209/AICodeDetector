
  with ops.name_scope(name, values=[x]):
    x = ops.convert_to_tensor(x, name="x")
    assertions = [
        check_ops.assert_non_negative(
            x, message="Elements must be non-negative."),
    ]
    if not x.dtype.is_integer:
      assertions += [
          check_ops.assert_integer(
              x, message="Elements must be integer."),
      ]
    return control_flow_ops.with_dependencies(assertions, x)


@tf_export("nn.embedding_lookup")
def