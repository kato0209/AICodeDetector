import java.util.Scanner;

public class LoanCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Prompt the user to enter the loan amount and loan period
        System.out.print("Loan Amount: ");
        double loanAmount = input.nextDouble();
        System.out.print("Number of Years: ");
        int numberOfYears = input.nextInt();

        // Display the table header
        System.out.printf("%-15s%-15s%-15s\n", "Interest Rate", "Monthly Payment", "Total Payment");

        // Compute and display the monthly and total payments for each interest rate
        for (double annualInterestRate = 5.0; annualInterestRate <= 8.0; annualInterestRate += 0.125) {
            double monthlyInterestRate = annualInterestRate / 1200.0;
            double monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / Math.pow(1 + monthlyInterestRate, numberOfYears * 12));
            double totalPayment = monthlyPayment * numberOfYears * 12;

            // Display the results for the current interest rate
            System.out.printf("%-15.3f%-15.2f%-15.2f\n", annualInterestRate, monthlyPayment, totalPayment);
        }
    }
}
