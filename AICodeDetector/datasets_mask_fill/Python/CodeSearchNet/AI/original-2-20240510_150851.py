
        if self.save_path is None:
            raise ValueError("No save path specified")
        if not os.path.isdir(self.save_path):
            os.makedirs(self.save_path)
        self.save_path = os.path.join(self.save_path, 'params.pkl')
        with open(self.save_path, 'wb') as f:
            pickle.dump(self.params, f)
        if exclude_scopes:
            for scope in exclude_scopes:
                if scope in