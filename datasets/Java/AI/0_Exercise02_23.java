import java.util.Scanner;

public class TripCostCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the driving distance: ");
        double distance = input.nextDouble();
        System.out.print("Enter the fuel efficiency of the car in miles per gallon: ");
        double mpg = input.nextDouble();
        System.out.print("Enter the price per gallon of fuel: ");
        double pricePerGallon = input.nextDouble();
        
        // Calculate the cost of the trip
        double gallonsUsed = distance / mpg;
        double tripCost = gallonsUsed * pricePerGallon;
        
        // Display the result
        System.out.printf("The cost of driving %.2f miles at %.2f miles per gallon and $%.2f per gallon is $%.2f.%n",
            distance, mpg, pricePerGallon, tripCost);
    }
}