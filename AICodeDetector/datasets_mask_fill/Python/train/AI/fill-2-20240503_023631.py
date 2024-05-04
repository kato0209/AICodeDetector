import tensorflow as tf

def feed_forward_network(v, dff):
    return tf.keras.Sequential([
    v   1  # First dense layer
       v2  # Second dense layer
    ])

# Example b = 512  # Dimensionality of the output space
dff = 2048     # Dimensionality of the feed-forward layer

ffn = feed_forward_network(d_model, dff)
ffn.summary()
