

    """Specialized inversion sampler for 3D."""
    if seed is not None:
        np.random.seed(seed)
    
    u = np.random.uniform(0, 1, n)
    v = np.random.uniform(0, 1, n)
    w = np.random.uniform(0, 1, n)
    
    x = self.inverse_transform_x(u)
    y = self.inverse_transform_y(v)
    z = self.inverse_transform_z(w)
    
    return np.column_stack((x, y, z