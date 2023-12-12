import java.util.Scanner;

public class PhoneKeyPads {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a phone number: ");
        String phoneNumber = input.nextLine();

        String translatedNumber = "";
        for (int i = 0; i < phoneNumber.length(); i++) {
            char ch = phoneNumber.charAt(i);
            if (Character.isLetter(ch)) {
                translatedNumber += getNumber(Character.toUpperCase(ch));
            } else {
                translatedNumber += ch;
            }
        }

        System.out.println("The translated phone number is: " + translatedNumber);
    }

    public static int getNumber(char uppercaseLetter) {
        if (uppercaseLetter >= 'A' && uppercaseLetter <= 'C') {
            return 2;
        } else if (uppercaseLetter >= 'D' && uppercaseLetter <= 'F') {
            return 3;
        } else if (uppercaseLetter >= 'G' && uppercaseLetter <= 'I') {
            return 4;
        } else if (uppercaseLetter >= 'J' && uppercaseLetter <= 'L') {
            return 5;
        } else if (uppercaseLetter >= 'M' && uppercaseLetter <= 'O') {
            return 6;
        } else if (uppercaseLetter >= 'P' && uppercaseLetter <= 'S') {
            return 7;
        } else if (uppercaseLetter >= 'T' && uppercaseLetter <= 'V') {
            return 8;
        } else if (uppercaseLetter >= 'W' && uppercaseLetter <= 'Z') {
            return 9;
        } else {
            return -1; // Invalid character
        }
    }
}