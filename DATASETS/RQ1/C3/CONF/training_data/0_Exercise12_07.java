public static int bin2Dec(String binaryString) throws NumberFormatException {
    int decimal = 0;
    for (int i = 0; i < binaryString.length(); i++) {
        char ch = binaryString.charAt(i);
        if (ch < '0' || ch > '1') {
            throw new NumberFormatException("Invalid binary string: " + binaryString);
        }
        decimal = decimal * 2 + (ch - '0');
    }
    return decimal;
}