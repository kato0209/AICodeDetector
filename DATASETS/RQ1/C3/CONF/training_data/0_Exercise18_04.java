public class Series {

    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            System.out.printf("m(%d) = %.2f%n", i, computeSeries(i));
        }
    }

    public static double computeSeries(int i) {
        if (i == 1) {
            return 1.0;
        } else {
            return computeSeries(i - 1) + 1.0 / i;
        }
    }
}
