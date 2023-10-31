import java.util.Scanner;

public class ShippingCost {
    public static void main(String[] args) {
        // Create a scanner to get input from the user
        Scanner input = new Scanner(System.in);

        // Prompt the user to enter the weight of the package
        System.out.print("Enter the weight of the package in pounds: ");
        double weight = input.nextDouble();

        // Calculate the shipping cost based on the weight
        double cost;
        if (weight > 50) {
            System.out.println("The package cannot be shipped.");
        } else if (weight > 10) {
            cost = 10.5;
            System.out.printf("The shipping cost is $%.2f\n", cost);
        } else if (weight > 3) {
            cost = 8.5;
            System.out.printf("The shipping cost is $%.2f\n", cost);
        } else if (weight > 1) {
            cost = 5.5;
            System.out.printf("The shipping cost is $%.2f\n", cost);
        } else if (weight > 0) {
            cost = 3.5;
            System.out.printf("The shipping cost is $%.2f\n", cost);
        } else {
            System.out.println("The weight must be greater than 0.");
        }
    }
}