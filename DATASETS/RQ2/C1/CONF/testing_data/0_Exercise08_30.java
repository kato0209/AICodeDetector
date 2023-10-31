public static double[] linearEquation(double[][] a, double[] b) {
    double determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0];
    if (determinant == 0) {
        System.out.println("The equation has no solution.");
        return null;
    } else {
        double x = (b[0] * a[1][1] - b[1] * a[0][1]) / determinant;
        double y = (b[1] * a[0][0] - b[0] * a[1][0]) / determinant;
        return new double[] {x, y};
    }
}   import java.util.Scanner;

public class LinearEquationTest {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a00, a01, a10, a11, b0, b1: ");
        double[][] a = {{input.nextDouble(), input.nextDouble()},
                        {input.nextDouble(), input.nextDouble()}};
        double[] b = {input.nextDouble(), input.nextDouble()};

        double[] solution = linearEquation(a, b);
        if (solution != null) {
            System.out.printf("x = %f, y = %f\n", solution[0], solution[1]);
        }
    }
}