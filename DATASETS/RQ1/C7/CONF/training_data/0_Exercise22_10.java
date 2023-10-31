
public class Main {
    public static void main(String[] args) {
        String fileName = "PrimeNumbers.dat";
        long[] primes = readPrimesFromFile(fileName);

        int[] numbers = {10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000L};

        System.out.printf("%12s %10s\n", "Number", "Primes");
        System.out.println("------------------------");

        for (int i = 0; i < numbers.length; i++) {
            int count = countPrimes(primes, numbers[i]);
            System.out.printf("%12d %10d\n", numbers[i], count);
        }
    }

    public static long[] readPrimesFromFile(String fileName) {
        try (DataInputStream input = new DataInputStream(new FileInputStream(fileName))) {
            int size = input.readInt();
            long[] primes = new long[size];

            for (int i = 0; i < size; i++) {
                primes[i] = input.readLong();
            }

            return primes;
        } catch (IOException e) {
            e.printStackTrace();
        }

        return null;
    }

    public static int countPrimes(long[] primes, int n) {
        int count = 0;

        for (int i = 0; i < primes.length; i++) {
            if (primes[i] <= n) {
                count++;
            } else {
                break;
            }
        }

        return count;
    }
}
