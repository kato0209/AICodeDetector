public class Conversion {
    
    public static double footToMeter(double foot) {
        return 0.305 * foot;
    }
    
    public static double meterToFoot(double meter) {
        return 3.279 * meter;
    }

    public static void main(String[] args) {
        System.out.println("Feet   Meters | Meters Feet");
        System.out.println("___________________________");
        for (double i = 1.0, j = 20.0; i <= 10.0; i++, j += 5) {
            System.out.printf("%-7.1f%-7.3f | %-7.1f%-7.3f\n", i, footToMeter(i), j, meterToFoot(j));
        }
    }
}
