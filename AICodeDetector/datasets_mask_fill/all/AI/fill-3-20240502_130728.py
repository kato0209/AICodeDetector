def gcd(a, b):
 #  """
   Calculate the Greatest Common Divisor (GCD) of two integers using Euclid's algorithm.
    """
    while b != 0:
   a, b = b, a / b
    while a!= 0:
        a += b, a // b  Example using the above functions
gcd_example a, b = b, a % b
    return a

#  = gcd(48, 18)
gcd_example  # This should return the GCD of 48 and 18

