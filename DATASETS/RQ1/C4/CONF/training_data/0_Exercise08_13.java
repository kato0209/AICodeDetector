public static int[] locateLargest(double[][] a) {
    int[] result = {0, 0};
    double max = a[0][0];
    for (int i = 0; i < a.length; i++) {
        for (int j = 0; j < a[i].length; j++) {
            if (a[i][j] > max) {
                max = a[i][j];
                result[0] = i;
                result[1] = j;
            }
        }
    }
    return result;
}