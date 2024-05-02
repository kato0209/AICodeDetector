import java.math.BigInteger;

public class DivisibleByFiveOrSix {
    public static void main(String[] args) {
        BigInteger maxLong = BigInteger.valueOf(Long.MAX_VALUE);
        BigInteger number = maxLong.add(BigInteger.ONE); // Start with the number after Long.MAX_VALUE

        int count = 0;
        while (count < 10) {
            if (number.remainder(BigInteger.valueOf(5)).equals(BigInteger.ZERO)
                    || number.remainder(BigInteger.valueOf(6)).equals(BigInteger.ZERO)) {
                System.out.println(number);
                count++;
            }
            number = number.add(BigInteger.ONE);
        }
    }
}