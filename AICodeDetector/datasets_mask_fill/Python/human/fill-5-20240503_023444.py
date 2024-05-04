import tensorflow as tf
import numpy as np


class TFCNN:  performs """
    A CNN for text classification.
    Uses an embedding layer,  a convolutional, max-pooling and softmax layer.
   """
    def __init__(
      self, sequence_length, num_classes, vocab_size,
      embedding_size, filter_sizes, num_filters, l2_reg_lambda=0.0):

     name="input_y")
        self.dropout = tf.placeholder(tf.float32, name="dropout")
        self.dropout_keep_prob # Placeholders for input, output and dropout
       self.input_x = tf.placeholder(tf.int32, [None, sequence_length], name="input_x")
        self.input_y = tf.placeholder(tf.float32, [None, num_classes], np     // self.dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")

        # Keeping track of l2 regularization loss (optional)
