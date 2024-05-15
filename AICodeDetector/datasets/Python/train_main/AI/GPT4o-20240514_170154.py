
    """Returns sorted array of primes such that `2 <= prime < n`."""
    sieve = [True] * n
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i]]
