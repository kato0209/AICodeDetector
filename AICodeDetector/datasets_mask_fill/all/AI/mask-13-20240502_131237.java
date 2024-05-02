public class GCD {
  <extra_id_0> void main(String[] args) {
   <extra_id_1> num1 = 24, num2 = 60, gcd = 1;
    for(int <extra_id_2> 1; i <= num1 && i <= num2; ++i)
   <extra_id_3>        <extra_id_4> i==0 && num2 % i==0)
       <extra_id_5>    <extra_id_6> i;
    }
    System.out.println("GCD of " <extra_id_7> +" and " + num2 + " is: " + gcd);
  }
}


public <extra_id_8> {
  public static int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
  }
 