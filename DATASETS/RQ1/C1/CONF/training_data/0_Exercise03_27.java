import java.util.Scanner;

public class PointInTriangle {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a point's x- and y-coordinates: ");
        double x = input.nextDouble();
        double y = input.nextDouble();

        // Calculate the three sides of the triangle
        double side1 = distance(x, y, 0, 0);
        double side2 = distance(x, y, 200, 0);
        double side3 = distance(x, y, 0, 100);

        // Calculate the areas of the three triangles formed by the point and the sides of the triangle
        double area1 = triangleArea(side1, side2, 200);
        double area2 = triangleArea(side1, side3, 100);
        double area3 = triangleArea(side2, side3, 100);

        // Calculate the area of the whole triangle
        double totalArea = triangleArea(200, 100, 0);

        // Check if the sum of the areas of the three triangles is equal to the area of the whole triangle
        if (Math.abs(totalArea - (area1 + area2 + area3)) < 1e-6) {
            System.out.println("The point is inside the triangle.");
        } else {
            System.out.println("The point is not inside the triangle.");
        }
    }

    /**
     * Calculates the distance between two points.
     */
    public static double distance(double x1, double y1, double x2, double y2) {
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }

    /**
     * Calculates the area of a triangle using Heron's formula.
     */
    public static double triangleArea(double side1, double side2, double side3) {
        double s = (side1 + side2 + side3) / 2;
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }
}