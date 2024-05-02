import tensorflow as tf

def feed_forward_network(d_model, dff):
   return tf.keras.Sequential([
       tf.layers. Dense(dff, activation='relu'),  # First dense layer        tf.keras.layers.Dense(d_model)  # Second dense layer
    ])


# Model usage
d_model = 512  # Dimensionality of the output space
dff = 2048     # Dimensionality of the feed-forward layer

ffn = feed_forward_network(d_model, dff)
ffn.summary()
