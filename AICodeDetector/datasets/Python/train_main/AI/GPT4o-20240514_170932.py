

    """Save model parameters to self.save_path"""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(self.save_path), exist_ok=True)
    
    # Filter out parameters to exclude
    state_dict = {k: v for k, v in self.state_dict().items() if not any(scope in k for scope in exclude_scopes)}
    
    # Save the state_dict
    torch.save(state_dict, self.save_path)
