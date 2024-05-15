
    """Makes a function which applies a list of Bijectors' `forward`s."""
        for b in bijector:
            x = b.forward(x)
        return x
    return transform
