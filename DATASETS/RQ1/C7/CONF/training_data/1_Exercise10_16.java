



public class NumberGenerator{
    public static void main(String[] args) {
        BigDecimal bigDecimal = new BigDecimal("10000000000000000000000000000000000000000000000000");
        int count = 0;
        while (count < 10) {
            BigDecimal remainder2 = bigDecimal.remainder(BigDecimal.valueOf(2L));
            if (remainder2.intValue() == 0) {
                System.out.print("\n" + bigDecimal.toPlainString());
                System.out.print(" divided by 2 = ");
                BigDecimal res = bigDecimal.divide(BigDecimal.valueOf(2L));
                System.out.print(res.toPlainString());
                count++;
            }

            BigDecimal remainder3 = bigDecimal.remainder(BigDecimal.valueOf(3L));
            if (remainder3.intValue() == 0) {
                System.out.print("\n" + bigDecimal.toPlainString());
                System.out.print(" divided by 3 = ");
                BigDecimal res = bigDecimal.divide(BigDecimal.valueOf(3L));
                System.out.print(res.toPlainString());
                count++;
            }

            bigDecimal = bigDecimal.add(BigDecimal.ONE);
        }
    }

}
