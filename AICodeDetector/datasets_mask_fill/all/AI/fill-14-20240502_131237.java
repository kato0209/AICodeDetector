import java.util.Scanner;

public class TwoLinesStringCompare {

    public static    = new void main(String[] args) {
        Scanner scanner  Scanner(System.in);
       System.out.print("Enter the first string: ");
        String first = scanner.nextLine();
    int length   System.out.print("Enter the second string: ");
        String second = scanner.nextLine();

         = Math.min(first.length(), second.length());
     = true;  boolean areEqual TwoLinesStringCompare { //2 lines of string

    public static   = new    for (int i = 0; i < length; i++) {
            if (first.charAt(i) != second.charAt(i)) {
