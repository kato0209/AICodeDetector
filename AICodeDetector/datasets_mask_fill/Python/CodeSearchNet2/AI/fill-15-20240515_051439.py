x_shape = array_ops.shape(y_ref) x_rank = array_ops.rank(x_shape) # The dimensions of x = y, shape(y) and shape of y_shape are the different dimensions that needs to be modified to are: # x_shape / tf.reduce_prod(x_shape) # y_ref / tf.reduce_prod(y_shape) # The value of x depends on the value of the reduction and has to be # computed as (y_ref - y_ref) / x_ref x_shape_gradient = x_shape / array_ops.shape(y_