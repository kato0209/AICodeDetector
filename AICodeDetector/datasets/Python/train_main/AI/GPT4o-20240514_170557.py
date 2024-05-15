

class DeepExponentialFamilyVariational(tf.keras.Model):
        super(DeepExponentialFamilyVariational, self).__init__()
        self.data_size = data_size
        self.feature_size = feature_size
        self.units = units

        self.encoder = tf.keras.Sequential([
            layers.InputLayer(input_shape=(data_size, feature_size)),
            layers.Dense(units, activation='relu'),
            layers.Dense(units, activation='relu')
        ])

        self.z_mean = layers.Dense(units