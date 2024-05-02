public class GCD {
  public static void main(String[] args) {
   int num1 = 24, num2 = 60, gcd = 1;
    for(int i = 1; i <= num1 && i <= num2; ++i)
   {
      if(num1 %        gcd = gcd * i;
      else                             gcd = gcd * num2;
      num2 = num2 % i==0 && num2 % i==0)
       + num1    class GCD i;
    }
    System.out.println("GCD of " public static void main(String[] args) +" and " + num2 + " is: " + gcd);
  }
}


public {
    int num = 0; {
  public static int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
  }
 