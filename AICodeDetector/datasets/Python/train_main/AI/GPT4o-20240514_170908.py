
    """Saves model to the save_path, provided in config. The directory is
    already created by super().__init__, which is called in __init__ of this class"""
    save_path = self.config.get('save_path')
    if save_path:
        with open(save_path, 'wb') as f:
            pickle.dump(self.model, f)
    else:
        raise ValueError("Save path not provided in config")
