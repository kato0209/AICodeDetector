# <extra_id_0> that observation index points and observation <extra_id_1> broadcast. ndims = kernel.feature_ndims if (tensorshape_util.is_fully_defined( observation_index_points.shape[:-ndims]) and tensorshape_util.is_fully_defined(observations.shape)): index_point_count = observation_index_points.shape[:-ndims] observation_count = observations.shape try: tf.broadcast_static_shape(index_point_count, observation_count) except ValueError: # <extra_id_2> with our own more contextual error message. raise ValueError( 'Observation index <extra_id_3> and observation counts are not ' 'broadcastable: {} and {}, respectively.'.format( index_point_count, observation_count))