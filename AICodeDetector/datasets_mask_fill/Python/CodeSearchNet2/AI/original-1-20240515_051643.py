
        if self.load_path is None:
            raise ValueError("No model parameters found in {}".format(self.load_path))
        self.load_path = os.path.expanduser(self.load_path)
        self.load_path = os.path.expandvars(self.load_path)
        self.load_path = os.path.expanduser(self.load_path)
        self.load_path = os.path.expandvars(self.load_path)
        self.load_path = os.path.expanduser(self.load_path)
        self.