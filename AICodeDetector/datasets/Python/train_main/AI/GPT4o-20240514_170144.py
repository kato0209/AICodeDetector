
    """Validate `outcomes`, `logits` and `probs`'s shapes."""
    if not validate_args:
        return

    if logits is not None and probs is not None:
        raise ValueError("Cannot specify both `logits` and `probs`.")

    if logits is not None:
        if outcomes.shape[-1] != logits.shape[-1]:
            raise ValueError("The last dimension of `outcomes` must match the last dimension of `logits`.")
    elif probs is not None:
