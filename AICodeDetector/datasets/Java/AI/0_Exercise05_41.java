import java.util.Scanner;

public class LargestOccurrence {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Prompt the user to enter integers
        System.out.print("Enter integers (end with 0): ");

        // Initialize variables for the largest number and its occurrence count
        int largest = 0;
        int count = 0;

        // Read and process the integers entered by the user
        int number = input.nextInt();
        while (number != 0) {
            if (number > largest) {
                largest = number;
                count = 1;
            } else if (number == largest) {
                count++;
            }
            number = input.nextInt();
        }

        // Display the result
        System.out.println("The largest number is " + largest);
        System.out.println("The occurrence count of the largest number is " + count);
    }
}
