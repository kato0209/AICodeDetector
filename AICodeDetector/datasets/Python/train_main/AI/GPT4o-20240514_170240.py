

class Model:
        self.latent_size = latent_size
        self.dense_layer = tf.keras.layers.Dense(latent_size * 2)  # For mean and log_std

        batch_shape = tf.shape(inputs)[:-1]
        hidden_size = inputs.shape[-1]
        
        # Flatten the inputs to apply the dense layer
        flat_inputs = tf.reshape(inputs, [-1, hidden_size])
        
        # Apply the dense layer to get the parameters for the