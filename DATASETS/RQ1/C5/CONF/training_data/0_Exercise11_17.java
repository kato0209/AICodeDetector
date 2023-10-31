import java.util.ArrayList;
import java.util.Scanner;

public class PerfectSquare {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        System.out.print("Enter an integer m: ");
        int m = input.nextInt();

        
        ArrayList<Integer> factors = new ArrayList<>();
        int factor = 2;
        while (factor <= m) {
            if (m % factor == 0) {
                factors.add(factor);
                m /= factor;
            } else {
                factor++;
            }
        }

        
        ArrayList<Integer> oddFactors = new ArrayList<>();
        for (int i = 0; i < factors.size(); i++) {
            int count = 1;
            for (int j = i + 1; j < factors.size(); j++) {
                if (factors.get(i).equals(factors.get(j))) {
                    count++;
                    i++;
                } else {
                    break;
                }
            }
            if (count % 2 == 1) {
                oddFactors.add(factors.get(i));
            }
        }

        
        int n = 1;
        for (int factor2 : oddFactors) {
            n *= factor2;
        }

        
        System.out.println("The smallest number n for m * n to be a perfect square is " + n);
        System.out.println("m * n is " + (m * n));
    }
}
