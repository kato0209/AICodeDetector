
    image_shape = tf.shape(input=inputs)[-3:]
    collapsed_shape = tf.concat(([-1], image_shape), axis=0)
    out = tf.reshape(inputs, collapsed_shape)  # (sample*batch*T, h, w, c)
    out = self.conv1(out)
    out = self.conv2(out)
    out = self.conv3(out)
    out = self.conv4(out)
    expanded_shape = tf.concat((tf.shape(input=inputs)[:-3], [-1]), axis=0)
    return tf.reshape(out, expanded_shape)