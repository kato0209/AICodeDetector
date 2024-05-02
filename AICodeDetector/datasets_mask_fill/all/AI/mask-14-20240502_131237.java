import java.util.Scanner;

public class <extra_id_0>    <extra_id_1> void main(String[] args) {
        Scanner scanner <extra_id_2> Scanner(System.in);
 <extra_id_3>      System.out.print("Enter the first string: ");
        String first = scanner.nextLine();
    <extra_id_4>   System.out.print("Enter the second string: ");
        String second = scanner.nextLine();

        <extra_id_5> = Math.min(first.length(), second.length());
     <extra_id_6>  boolean areEqual <extra_id_7>   <extra_id_8>    for (int i = 0; i < length; i++) {
            if (first.charAt(i) != second.charAt(i)) {
