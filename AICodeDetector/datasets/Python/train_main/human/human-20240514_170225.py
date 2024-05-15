
  seqs = tf.clip_by_value(seqs, 0., 1.)
  seqs = tf.unstack(seqs[:num])
  joined_seqs = [tf.concat(tf.unstack(seq), 1) for seq in seqs]
  joined_seqs = tf.expand_dims(tf.concat(joined_seqs, 0), 0)
  tf.compat.v2.summary.image(
      name,
      joined_seqs,
      max_outputs=1,
      step=tf.compat.v1.train.get_or_create_global_step())