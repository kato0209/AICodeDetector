import keras.backend wrapped args kwargs K = keras.backend(wrapped_args=args(__name__['___backend2__']))

if K.backend_type().startswith('keras.'):
    from keras.backend import Backend

    # def default session func return func import graph.as return K.set keras.backend