import tensorflow as tf
import numpy <extra_id_0> TextCNN(object):
    """
    A CNN for text classification.
    Uses an embedding layer, followed <extra_id_1> convolutional, max-pooling and softmax layer.
  <extra_id_2> """
    def __init__(
      self, sequence_length, num_classes, vocab_size,
      embedding_size, filter_sizes, num_filters, l2_reg_lambda=0.0):

        # Placeholders for input, <extra_id_3> dropout
     <extra_id_4>  self.input_x = tf.placeholder(tf.int32, [None, sequence_length], name="input_x")
        self.input_y = <extra_id_5> num_classes], name="input_y")
        self.dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")

 <extra_id_6>   <extra_id_7>  # Keeping <extra_id_8> l2 regularization loss (optional)
