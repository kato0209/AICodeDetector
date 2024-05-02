class SieveOfEratosthenes {
    void sieveOfEratosthenes(int n) {
     <extra_id_0>  <extra_id_1> a boolean array "prime[0..n]" and initialize
    <extra_id_2>   // all <extra_id_3> as true. A value in <extra_id_4>     <extra_id_5>  // <extra_id_6> false <extra_id_7> is Not a prime, else true.
        boolean <extra_id_8> new boolean[n+1];
        for(int i=0;i<n;i++)
            prime[i] = true;

        for(int p = 2; p*p <=n; p++) {
            // If prime[p] is not