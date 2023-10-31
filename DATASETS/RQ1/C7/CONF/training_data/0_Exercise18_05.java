public class Series {
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            System.out.println("m(" + i + ") = " + computeM(i));
        }
    }

    public static double computeM(int i) {
        if (i == 1) {
            return 1.0/3;
        } else {
            return i/(2.0*i + 1) + computeM(i - 1);
        }
    }
}


