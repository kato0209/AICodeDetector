

    """Compute the harmonic number from its analytic continuation.

    Derivation from [here](
    https://en.wikipedia.org/wiki/Digamma_function#Relation_to_harmonic_numbers)
    and [Euler's constant](
    https://en.wikipedia.org/wiki/Euler%E2%80%93Mascheroni_constant).

    Args:
        x: input float.

    Returns:
        z: The analytic continuation of the harmonic number for the input.
    """
    return math.psi(x + 1) + math.euler_gamma
