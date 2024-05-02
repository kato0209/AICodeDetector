import tensorflow as tf

def feed_forward_network(d_model, dff):
 <extra_id_0>  return tf.keras.Sequential([
       <extra_id_1> activation='relu'),  # First <extra_id_2>        tf.keras.layers.Dense(d_model)  # Second dense layer
    <extra_id_3> usage
d_model = 512  <extra_id_4> of the output space
dff = 2048     # Dimensionality of the feed-forward layer

ffn = feed_forward_network(d_model, dff)
ffn.summary()
