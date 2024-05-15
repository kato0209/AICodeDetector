

class ModelLoader:
        self.model_path = model_path
        self.model = None

        """Checks existence of the model file, loads the model if the file exists"""
        if os.path.exists(self.model_path):
            with open(self.model_path, 'rb') as file:
                self.model = pickle.load(file)
