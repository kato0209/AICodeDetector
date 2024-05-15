

    """Helper to broadcast a tensor using a list of target tensors."""
    # Determine the target shape by finding the maximum shape along each dimension
    target_shape = np.broadcast(*target_tensors).shape
    
    # Broadcast the tensor to the target shape
    broadcasted_tensor = np.broadcast_to(tensor_to_broadcast, target_shape)
    
    return broadcasted_tensor
