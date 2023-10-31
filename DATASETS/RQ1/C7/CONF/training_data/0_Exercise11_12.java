
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<Double> list = new ArrayList<>();

        System.out.print("Enter 5 numbers: ");
        for (int i = 0; i < 5; i++) {
            double number = input.nextDouble();
            list.add(number);
        }

        double sum = sum(list);
        System.out.println("The sum of the numbers is " + sum);
    }

    public static double sum(ArrayList<Double> list) {
        double sum = 0;
        for (double number : list) {
            sum += number;
        }
        return sum;
    }
}
