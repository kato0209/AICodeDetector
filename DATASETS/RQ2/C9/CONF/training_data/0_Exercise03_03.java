import java.util.Scanner;

public class CramersRule {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt user to enter values for a, b, c, d, e, and f
        System.out.print("Enter a, b, c, d, e, and f: ");
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();
        double d = scanner.nextDouble();
        double e = scanner.nextDouble();
        double f = scanner.nextDouble();

        // Calculate the determinant and check if it's zero
        double determinant = a * d - b * c;
        if (determinant == 0) {
            System.out.println("The equation has no solution.");
        } else {
            // Calculate x and y using Cramer's rule
            double x = (e * d - b * f) / determinant;
            double y = (a * f - e * c) / determinant;

            // Display the result
            System.out.printf("x is %.2f and y is %.2f\n", x, y);
        }

        scanner.close();
    }
}