
  average = lambda dist: tf.reduce_mean(
      input_tensor=dist.mean(), axis=0)  # avg over samples
  with tf.compat.v1.name_scope("val_reconstruction"):
    reconstruct = functools.partial(model.reconstruct, inputs=inputs,
                                    samples=samples)
    visualize_reconstruction(inputs, average(reconstruct()))
    visualize_reconstruction(inputs, average(reconstruct(sample_static=True)),
                             name="static_prior")
    visualize_reconstruction(inputs, average(reconstruct(sample_dynamic=True)),
                   