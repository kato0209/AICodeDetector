
    """
    Creates the basic network architecture,
    transforming word embeddings to intermediate outputs
    """

    # Define a simple feed-forward neural network
    hidden_layer = tf.keras.layers.Dense(units=128, activation='relu')(word_outputs)
    dropout_layer = tf.keras.layers.Dropout(rate=0.5)(hidden_layer)
    output_layer = tf.keras.layers.Dense(units=64, activation='relu')(dropout_layer)

    return output_layer
