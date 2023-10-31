import java.util.Scanner;

public class DistanceBetweenPoints {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the x-coordinate of the first point: ");
        double x1 = input.nextDouble();
        System.out.print("Enter the y-coordinate of the first point: ");
        double y1 = input.nextDouble();
        System.out.print("Enter the x-coordinate of the second point: ");
        double x2 = input.nextDouble();
        System.out.print("Enter the y-coordinate of the second point: ");
        double y2 = input.nextDouble();

        double distance = Math.pow(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2), 0.5);

        System.out.println("The distance between the two points is " + distance);
    }
}