



public class CombinationsCalculator{
    public static void main(String[] args) {

        int count = 0;
        for (int n = 1; n < 7; n++) {
            for (int j = n + 1; j <= 7; j++) {
                System.out.println(n + " " + j);
                count++;
            }
        }
        System.out.println("Total combinations -> " + count);
    }
}
