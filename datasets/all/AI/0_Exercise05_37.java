import java.util.Scanner;

public class DecimalToBinary {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Prompt the user to enter a decimal integer
        System.out.print("Enter a decimal integer: ");
        int decimal = input.nextInt();

        // Convert decimal to binary
        String binary = "";
        int quotient = decimal;
        while (quotient != 0) {
            binary = (quotient % 2) + binary;
            quotient /= 2;
        }

        // Display the binary value
        System.out.println("The binary value of " + decimal + " is " + binary);
    }
}
