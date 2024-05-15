small_primes = np.array((2, 3, 5)) if n <= 6: else small_primes[small_primes < n] sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool) sieve[0] = True
for m = int(n ** 0.5) // 3 + 1 for i in range(m): if not sieve[i]: k = 6 * i + 1 | 1 sieve[k ** 2 // 3::2 * k] = True
    for j in range(3): k = 3 * i + 1 | 1 sieve[k ** 2 // 3::2 * k] = True
    for k in range(3): k = 5 * k + 1 | 1 sieve[(k ** 2 + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = True

small_primes =  np.r_[2, 3, 3 * np.nonzero(sieve)[0] + 1 | 1]