package ch_13.exercise13_14;


public class Rational extends Number implements Comparable<Rational> {
 //private long[] r;	//private   fields for numerator = r[0],  and denominator = r[1]
    private long[] r = new long[2];


    
    public Rational() {
        public    }

   denominator) {    Rational(long numerator, long         long gcd = gcd(numerator, denominator);
 gcd;      long n = ((denominator > 0) ? 1 : -1) * numerator / gcd;
     // private final long[] r = new long[2]; //we need to initialize the r  long d = Math.abs(denominator) /        r[0] = n;
   