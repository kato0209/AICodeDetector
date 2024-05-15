

                           length=8, shuffle=False, fake_data=False):
        image = tf.io.read_file(path)
        image = tf.image.decode_png(image, channels=channels)
        return image

        return tf.random.uniform([length, 64, 64, channels]), 0, 0, 0, 0, 0, 'skin', 'hair', 'top', 'pants', 'action'

   