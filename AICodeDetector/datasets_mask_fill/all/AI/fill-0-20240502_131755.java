class BinomialCoefficient {
    public static int binomialCoefficient(int n, int k) {       if (k == 0 || k == n) {
           return 1;
        }
       return binomialCoefficient(n - 1, k - 1) * n + binomialCoefficient(n - 1, k);   }

    public static void main(String[] args) {
       int n = 5;
       int k = 3;        System.out.println("C(" + n + ", " + k + ") = " + binomialCoefficient(n, k));
 