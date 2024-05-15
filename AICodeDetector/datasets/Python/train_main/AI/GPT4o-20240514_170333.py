
    """Helper to validate block sizes."""
    if len(block_sizes) != len(bijectors):
        raise ValueError("block_sizes and bijectors must have the same length.")
    
    if validate_args:
        for size in block_sizes:
            if size <= 0:
                raise ValueError("All block sizes must be positive integers.")
