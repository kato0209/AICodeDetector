
        if not os.path.isfile(self.model_file):
            raise ValueError("Model file {} does not exist".format(self.model_file))
        if not os.access(self.model_file, os.R_OK):
            raise ValueError("Model file {} is not readable".format(self.model_file))
        self.model_file = os.path.abspath(self.model_file)
        self.model_file_exists = os.path.isfile(self.model_file)
        if not self.model_file_exists:
            raise ValueError("Model