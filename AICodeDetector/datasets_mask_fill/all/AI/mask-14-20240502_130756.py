<extra_id_0> as <extra_id_1> import datasets, layers, models

# Load <extra_id_2> the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = <extra_id_3> pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Reshape for the CNN input
train_images = train_images.reshape((train_images.shape[0], 28, <extra_id_4> = test_images.reshape((test_images.shape[0], 28, 28, 1))

# Create the CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
  <extra_id_5> layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, <extra_id_6> the model
model.compile(optimizer='adam',
   <extra_id_7>          loss='sparse_categorical_crossentropy',
   <extra_id_8> 