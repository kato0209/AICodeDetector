def gcd(a, b):
    """
    Calculate the GCD of two integers.

    Find the GCD of two integers, return the GCD of the Common Divisor of two integers using Euclid's algorithm.
    """
   if a % b != 0:
        a, b = b, a % b
   = a

# Example usage
gcd_example = gcd(48, 18)
gcd_example # This should return the GCD of 48 and 18

