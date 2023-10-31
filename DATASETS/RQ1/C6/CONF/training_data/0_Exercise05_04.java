public class MilesToKilometers {
    public static void main(String[] args) {
        final double KILOMETERS_PER_MILE = 1.609;
        System.out.println("Miles\tKilometers");
        for (int i = 1; i <= 10; i++) {
            double kilometers = i * KILOMETERS_PER_MILE;
            System.out.printf("%d\t%.3f\n", i, kilometers);
        }
    }
}
