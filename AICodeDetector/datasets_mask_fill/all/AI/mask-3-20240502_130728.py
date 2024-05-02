def gcd(a, b):
 <extra_id_0>  """
  <extra_id_1> Calculate the Greatest Common Divisor (GCD) of two integers using Euclid's algorithm.
    """
    while b != 0:
   <extra_id_2>  <extra_id_3> a, b = b, a % b
    return a

# <extra_id_4> = gcd(48, 18)
gcd_example  # This should return the GCD of 48 and 18

