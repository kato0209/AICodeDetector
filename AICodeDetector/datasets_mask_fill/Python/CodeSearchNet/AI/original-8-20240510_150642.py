
  data_gen = ImageDataGenerator(
      featurewise_center=True,  # set input mean to 0 over the dataset
      samplewise_center=True,  # set each sample mean to 0
      featurewise_std_normalization=True,  # divide inputs by std of the dataset
      samplewise_std_normalization=True,  # divide each input by its std
      zca_whitening=False,  # apply ZCA whitening
      rotation_range=20,  # randomly rotate images in the range (degrees, 0 to 180)
      width_shift_range=0