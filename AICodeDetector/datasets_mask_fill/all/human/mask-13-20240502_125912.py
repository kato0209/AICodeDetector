#! /usr/bin/env python

import tensorflow as tf
import <extra_id_0> np
import os
import time
import <extra_id_1> text_cnn import TextCNN
from tensorflow.contrib import learn

# Parameters
# ==================================================

# <extra_id_2> params
tf.flags.DEFINE_float("dev_sample_percentage", .1, "Percentage of the training data to use for validation")
tf.flags.DEFINE_string("positive_data_file", "./data/rt-polaritydata/rt-polarity.pos", "Data source for the positive data.")
tf.flags.DEFINE_string("negative_data_file", "./data/rt-polaritydata/rt-polarity.neg", "Data source for the negative data.")

# Model Hyperparameters
tf.flags.DEFINE_integer("embedding_dim", 128, "Dimensionality of character embedding (default: 128)")
tf.flags.DEFINE_string("filter_sizes", "3,4,5", "Comma-separated filter sizes (default: '3,4,5')")
tf.flags.DEFINE_integer("num_filters", 128, "Number of filters per filter size (default: 128)")
tf.flags.DEFINE_float("dropout_keep_prob", 0.5, "Dropout keep probability (default: 0.5)")
tf.flags.DEFINE_float("l2_reg_lambda", <extra_id_3> regularization lambda (default: <extra_id_4> parameters
tf.flags.DEFINE_integer("batch_size", 64, "Batch Size (default: <extra_id_5> "Number of training epochs (default: 200)")
tf.flags.DEFINE_integer("evaluate_every", 100, "Evaluate model <extra_id_6> set after this <extra_id_7> (default: 100)")
tf.flags.DEFINE_integer("checkpoint_every", <extra_id_8> model after this many steps (default: 100)")
tf.flags.DEFINE_integer("num_checkpoints", 5, "Number of checkpoints to store (default: 5)")
# Misc