public class SumDigits {
    public static int sumDigits(long n) {
        if (n == 0) {
            return 0;
        } else {
            return (int)(n % 10) + sumDigits(n / 10);
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        long n = input.nextLong();
        int sum = sumDigits(n);
        System.out.println("The sum of the digits is " + sum);
    }
}
