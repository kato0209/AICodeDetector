import java.util.Scanner;

public class RectangleOverlap {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Prompt the user to enter the center coordinates, width, and height of two rectangles
        System.out.println("Enter the center coordinates, width, and height of rectangle 1: ");
        double x1 = input.nextDouble();
        double y1 = input.nextDouble();
        double w1 = input.nextDouble();
        double h1 = input.nextDouble();

        System.out.println("Enter the center coordinates, width, and height of rectangle 2: ");
        double x2 = input.nextDouble();
        double y2 = input.nextDouble();
        double w2 = input.nextDouble();
        double h2 = input.nextDouble();

        // Determine the corner coordinates of each rectangle
        double x1Left = x1 - w1 / 2;
        double x1Right = x1 + w1 / 2;
        double y1Top = y1 - h1 / 2;
        double y1Bottom = y1 + h1 / 2;

        double x2Left = x2 - w2 / 2;
        double x2Right = x2 + w2 / 2;
        double y2Top = y2 - h2 / 2;
        double y2Bottom = y2 + h2 / 2;

        // Determine whether the two rectangles overlap, are contained, or don't overlap
        String message = "";
        if (x1Left <= x2Right && x1Right >= x2Left && y1Top <= y2Bottom && y1Bottom >= y2Top) {
            message = "The rectangles overlap.";
        } else if (x1Left >= x2Left && x1Right <= x2Right && y1Top >= y2Top && y1Bottom <= y2Bottom) {
            message = "Rectangle 1 is contained in rectangle 2.";
        } else if (x2Left >= x1Left && x2Right <= x1Right && y2Top >= y1Top && y2Bottom <= y1Bottom) {
            message = "Rectangle 2 is contained in rectangle 1.";
        } else {
            message = "The rectangles don't overlap.";
        }

        // Display the rectangles and the message
        System.out.println(message);
        System.out.println("Rectangle 1: (" + x1 + ", " + y1 + "), width = " + w1 + ", height = " + h1);
        System.out.println("Rectangle 2: (" + x2 + ", " + y2 + "), width = " + w2 + ", height = " + h2);
    }
}