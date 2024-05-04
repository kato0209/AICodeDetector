import tensorflow as tf
import numpy as <extra_id_0>  <extra_id_1> """
    A CNN for text classification.
    Uses an embedding layer, <extra_id_2> a convolutional, max-pooling and softmax layer.
  <extra_id_3> """
    def __init__(
      self, sequence_length, num_classes, vocab_size,
      embedding_size, filter_sizes, num_filters, l2_reg_lambda=0.0):

   <extra_id_4>  <extra_id_5> # Placeholders for input, output and dropout
   <extra_id_6>    self.input_x = tf.placeholder(tf.int32, [None, sequence_length], name="input_x")
        self.input_y = tf.placeholder(tf.float32, [None, num_classes], <extra_id_7>     <extra_id_8> self.dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")

        # Keeping track of l2 regularization loss (optional)
