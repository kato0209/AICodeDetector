import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a sequence of numbers (end with 0): ");
        int number;
        do {
            number = scanner.nextInt();
            if (number != 0) {
                list.add(number);
            }
        } while (number != 0);

        Integer max = max(list);
        if (max != null) {
            System.out.println("The largest number is " + max);
        } else {
            System.out.println("The list is empty.");
        }
    }

    public static Integer max(ArrayList<Integer> list) {
        if (list == null || list.size() == 0) {
            return null;
        }

        int max = list.get(0);
        for (int i = 1; i < list.size(); i++) {
            int number = list.get(i);
            if (number > max) {
                max = number;
            }
        }

        return max;
    }
}
