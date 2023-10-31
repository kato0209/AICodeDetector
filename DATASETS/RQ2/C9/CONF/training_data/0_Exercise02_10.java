import java.util.Scanner;

public class HeatEnergy {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the amount of water in kilograms: ");
        double weight = input.nextDouble();
        System.out.print("Enter the initial temperature of the water in degrees Celsius: ");
        double initialTemp = input.nextDouble();
        System.out.print("Enter the final temperature of the water in degrees Celsius: ");
        double finalTemp = input.nextDouble();
        
        // Calculate the energy needed
        double energy = weight * (finalTemp - initialTemp) * 4184;
        
        // Display the result
        System.out.printf("The energy needed to heat %.2f kilograms of water from %.2f°C to %.2f°C is %.2f joules.%n", weight, initialTemp, finalTemp, energy);
    }
}