import java.util.Scanner;

public class LoanAmortizationSchedule {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Get loan details from user
        System.out.print("Loan Amount: ");
        double loanAmount = input.nextDouble();

        System.out.print("Number of Years: ");
        int numberOfYears = input.nextInt();

        System.out.print("Annual Interest Rate: ");
        double annualInterestRate = input.nextDouble();

        // Calculate monthly interest rate
        double monthlyInterestRate = annualInterestRate / 1200;

        // Calculate monthly payment and total payment
        double monthlyPayment = loanAmount * monthlyInterestRate /
                (1 - 1 / Math.pow(1 + monthlyInterestRate, numberOfYears * 12));
        double totalPayment = monthlyPayment * numberOfYears * 12;

        // Display monthly payment and total payment
        System.out.printf("Monthly Payment: %.2f\n", monthlyPayment);
        System.out.printf("Total Payment: %.2f\n", totalPayment);

        // Display amortization schedule
        System.out.println("Payment#\tInterest\tPrincipal\tBalance");
        double balance = loanAmount;
        for (int i = 1; i <= numberOfYears * 12; i++) {
            double interest = monthlyInterestRate * balance;
            double principal = monthlyPayment - interest;
            balance -= principal;

            System.out.printf("%-10d\t%-10.2f\t%-10.2f\t%.2f\n", i, interest, principal, balance);

            // Check if balance is zero or negative
            if (balance <= 0) {
                // If balance is negative, add it to the last payment
                if (balance < 0) {
                    monthlyPayment += balance;
                    totalPayment = monthlyPayment * i;
                }
                break;
            }
        }

        // Display last payment if balance is not zero
        if (balance > 0) {
            System.out.printf("%-10d\t%-10.2f\t%-10.2f\t0.00\n", numberOfYears * 12, monthlyInterestRate * balance, balance);
        }
    }
}
