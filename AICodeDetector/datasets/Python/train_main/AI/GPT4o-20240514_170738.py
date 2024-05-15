

class JTensor:
        self.storage = storage
        self.shape = shape
        self.bigdl_type = bigdl_type

    @classmethod
        storage = a_ndarray.flatten()
        shape = np.array(a_ndarray.shape)
        return cls(storage, shape, bigdl_type)

        return self.storage.reshape(self.shape)
