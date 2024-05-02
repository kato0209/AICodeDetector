import java.util.Scanner;

public <extra_id_0> {
    public static void main(String[] args) {
        Scanner scanner = <extra_id_1>        System.out.print("Enter a string: ");
     <extra_id_2>  String input <extra_id_3>        System.out.print("Enter the word to be deleted: ");
     <extra_id_4>  String wordToDelete = scanner.nextLine();

  <extra_id_5>     String[] <extra_id_6> input.split(" ");
     <extra_id_7>  StringBuilder newString = new StringBuilder();
        for (String word : <extra_id_8>            if (!word.equals(wordToDelete)) {
    