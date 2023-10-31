public static int hex2Dec(String hexString) {
    if (hexString.length() == 0) {
        return 0;
    } else {
        int lastDigit = hexCharToDecimal(hexString.charAt(hexString.length() - 1));
        String remaining = hexString.substring(0, hexString.length() - 1);
        return hex2Dec(remaining) * 16 + lastDigit;
    }
}

public static int hexCharToDecimal(char ch) {
    if (ch >= '0' && ch <= '9') {
        return ch - '0';
    } else if (ch >= 'A' && ch <= 'F') {
        return ch - 'A' + 10;
    } else if (ch >= 'a' && ch <= 'f') {
        return ch - 'a' + 10;
    } else {
        throw new IllegalArgumentException("Invalid hex digit: " + ch);
    }
}


public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a hex string: ");
        String hexString = input.nextLine();
        int decimal = hex2Dec(hexString);
        System.out.println("The decimal equivalent is: " + decimal);
    }
}

