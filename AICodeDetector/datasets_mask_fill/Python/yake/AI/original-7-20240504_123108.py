def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using Euclid's algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
gcd_example = gcd(48, 18)
gcd_example  # This should return the GCD of 48 and 18

