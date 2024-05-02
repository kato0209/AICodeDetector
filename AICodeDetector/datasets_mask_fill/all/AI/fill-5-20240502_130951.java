class SieveOfEratosthenes {
    void sieveOfEratosthenes(int n) {
     // Create   a boolean array "prime[0..n]" and initialize
    elements to be primes   // all the boolean array "primes[i]" as true. A value in      <  // means that n false [] prime = is Not a prime, else true.
        boolean the boolean array contains the new boolean[n+1];
        for(int i=0;i<n;i++)
            prime[i] = true;

        for(int p = 2; p*p <=n; p++) {
            // If prime[p] is not