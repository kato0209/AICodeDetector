import java.util.Scanner;

public class CommonPrefix {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the first string: ");
        String str1 = scanner.nextLine();
        System.out.print("Enter the second string: ");
        String str2 = scanner.nextLine();
        
        // Find length of common prefix
        int len = Math.min(str1.length(), str2.length());
        int i;
        for (i = 0; i < len; i++) {
            if (str1.charAt(i) != str2.charAt(i)) {
                break;
            }
        }
        
        // Output common prefix
        String commonPrefix = str1.substring(0, i);
        if (commonPrefix.length() > 0) {
            System.out.println("The common prefix is: " + commonPrefix);
        } else {
            System.out.println("There is no common prefix.");
        }
    }
}