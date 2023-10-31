

import java.util.Scanner;


public class nan {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Enter two integers: ");
        int m = in.nextInt();
        int n = in.nextInt();

        System.out.println("The GCD of " + m + " and " + n + " is " + gcd(m, n));

    }

    static int gcd(int m, int n) {
        if (m % n == 0) {
            return n;
        }
        return gcd(n, m % n);
    }
}
