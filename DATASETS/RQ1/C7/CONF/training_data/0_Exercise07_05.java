
public class DistinctNumbers {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int[] numbers = new int[10];
        int distinctCount = 0;

        for (int i = 0; i < numbers.length; i++) {
            int number = input.nextInt();

            if (isNewNumber(numbers, number)) {
                numbers[distinctCount] = number;
                distinctCount++;
            }
        }

        System.out.println("Number of distinct numbers: " + distinctCount);
        System.out.print("Distinct numbers: ");

        for (int i = 0; i < distinctCount; i++) {
            System.out.print(numbers[i] + " ");
        }

        input.close();
    }

    public static boolean isNewNumber(int[] numbers, int number) {
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == number) {
                return false;
            }
        }

        return true;
    }
}
