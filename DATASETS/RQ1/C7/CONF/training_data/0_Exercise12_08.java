public class HexFormatException extends Exception {
    public HexFormatException(String message) {
        super(message);
    }
}

public class HexConverter {
    public static int hex2Dec(String hexString) throws HexFormatException {
        int decimalValue = 0;
        for (int i = 0; i < hexString.length(); i++) {
            char hexChar = hexString.charAt(i);
            if (!(hexChar >= '0' && hexChar <= '9') &&
                !(hexChar >= 'A' && hexChar <= 'F') &&
                !(hexChar >= 'a' && hexChar <= 'f')) {
                throw new HexFormatException("Invalid hex string: " + hexString);
            }
            decimalValue = decimalValue * 16 + hexToDecimal(hexChar);
        }
        return decimalValue;
    }

    public static int hexToDecimal(char ch) {
        if (ch >= 'A' && ch <= 'F')
            return 10 + ch - 'A';
        else
            return ch - '0';
    }
}
