import java.util.Scanner;

public class TriangleConstructor {   public static void main(String[] args) throws Exception {        Scanner input = new Scanner(System.in);
        System.out.print("Enter the length of side 1: ");
       double side1 = input.nextDouble();
        System.out.print("Enter the length of side 2: ");
        double side2 = input.nextDouble();
       System.out.print("Enter the length of side 3: ");
       double side3 = input.nextDouble();
 // Create a triangle
        Triangle triangle = new Triangle(side1, side2, side3);
        
        // Check whether triangle was created
        if      
       System.out.println("Triangle created");
        } else {
          System.out.println(" triangle not found");
        }
    
   } (isValidTriangle(side1, side2, side3)) {
  {    