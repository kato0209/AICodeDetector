import java.util.Random;
import java.util.Scanner;

public class ThreeSingleDigits {
    public static void main(String[] args) {
        // Create a Random object to generate random integers
        Random random = new Random();

        // Generate three single-digit integers
        int number1 = random.nextInt(10);
        int number2 = random.nextInt(10);
        int number3 = random.nextInt(10);

        // Calculate the sum of the three integers
        int sum = number1 + number2 + number3;

        // Prompt the user to enter the sum of the three integers
        Scanner input = new Scanner(System.in);
        System.out.print("What is the sum of " + number1 + " + " + number2 + " + " + number3 + "? ");
        int userSum = input.nextInt();

        // Check if the user's sum is correct and display the result
        if (userSum == sum) {
            System.out.println("Congratulations! Your answer is correct.");
        } else {
            System.out.println("Sorry, your answer is incorrect. The correct answer is " + sum + ".");
        }
    }
}