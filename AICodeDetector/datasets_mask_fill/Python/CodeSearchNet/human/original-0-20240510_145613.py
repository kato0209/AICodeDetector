
  flat_from = tf.nest.flatten(from_structure)
  flat_to = tf.nest.flatten(to_structure)
  if len(flat_from) == 1:
    flat_from *= len(flat_to)
  return tf.nest.pack_sequence_as(to_structure, flat_from)