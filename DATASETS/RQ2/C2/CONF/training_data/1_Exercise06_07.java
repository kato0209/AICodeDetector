

import java.util.*;


public class Exercise06_07 {
    static final int firstYear = 1;
    static final int lastYear = 30;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Enter the amount invested: ");
        double amount = in.nextDouble();

        System.out.println("The Annual interest rate as (ex: 5.25 for 5.25%:):  ");
        double yearRate = in.nextDouble();
        yearRate /= 100;

        double monthRate = yearRate / 12;

        System.out.println("Years --- Future Value ");

        for (int i = firstYear; i <= lastYear; i++) {
            System.out.print(i);
            System.out.printf("      %.2f", futureInvestmentValue(amount, monthRate, i));
            System.out.println();
        }

        in.close();
    }


    public static double futureInvestmentValue(double investmentAmount, double monthlyInterestRate, int years) {
        return investmentAmount * Math.pow(1 + monthlyInterestRate, years * 12);
    }
}