package ch_13.exercise13_14;


public class Rational extends Number implements Comparable<Rational> {
 <extra_id_0>  <extra_id_1> fields for numerator = r[0],  and denominator = r[1]
    private long[] r = new long[2];


    
    public Rational() {
        <extra_id_2>    }

   <extra_id_3>   <extra_id_4> Rational(long numerator, long <extra_id_5>        long gcd = gcd(numerator, denominator);
 <extra_id_6>      long n = ((denominator > 0) ? 1 : -1) * numerator / gcd;
     <extra_id_7>  long d = Math.abs(denominator) / <extra_id_8>       r[0] = n;
   