
  small_primes = np.array((2, 3, 5))
  if n <= 6:
    return small_primes[small_primes < n]
  sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
  sieve[0] = False
  m = int(n ** 0.5) // 3 + 1
  for i in range(m):
    if not sieve[i]:
      continue
    k = 3 * i + 1 | 1
    sieve[k ** 2 // 3::2 * k] = False
    sieve[(k ** 2 + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False
  return np.r_[2, 3, 3 * np.nonzero(sieve)[0] + 1 | 1]