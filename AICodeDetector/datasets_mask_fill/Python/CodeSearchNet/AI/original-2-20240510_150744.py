
        if not (weights_hdf5 is None or weights_hdf5 == ''):
            raise Exception("Weights file should be specified.")

        if by_name:
            if weights_hdf5.startswith('http'):
                self.load_weights_from_url(weights_hdf5)
            else:
                raise Exception("Weights file url should be http or https.")
        else:
            if