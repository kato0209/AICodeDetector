
    with tf.variable_scope("model", reuse=tf.AUTO_REUSE):
      # We use a different variable scope here because the variables are
      # shared across multiple models.
      # We also use the same variable scope name for both the model and
      # the non-model variables.
      with tf.variable_scope("model", reuse=tf.AUTO_REUSE):
        # We use the same variable scope name for both the model and
        # the non-model variables.
        with tf.variable_scope("non_model", reuse=tf.AUTO_REUSE):
          # We use