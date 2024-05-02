class BinomialCoefficient {
    public static int binomialCoefficient(int n, int k) <extra_id_0>       if (k == 0 || k == n) {
        <extra_id_1>   return 1;
        }
 <extra_id_2>      return binomialCoefficient(n - 1, k <extra_id_3> + binomialCoefficient(n - 1, <extra_id_4>   }

    public static void main(String[] args) {
     <extra_id_5>  int n = 5;
    <extra_id_6>   int k <extra_id_7>        System.out.println("C(" + n <extra_id_8> " + k + ") = " + binomialCoefficient(n, k));
 