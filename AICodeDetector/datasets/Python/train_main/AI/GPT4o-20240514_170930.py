
    """Load model parameters from self.load_path"""

    if not os.path.exists(self.load_path):
        raise FileNotFoundError(f"Load path {self.load_path} does not exist")

    checkpoint = torch.load(self.load_path, map_location=self.device)
    model_state_dict = checkpoint['model_state_dict']

    # Filter out parameters that are in the exclude_scopes
    filtered_state_dict = {k: v for k, v in model_state_dict.items() if not any(scope