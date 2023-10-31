public static void shuffle(int[][] m) {
    Random rand = new Random();
    for (int i = m.length - 1; i > 0; i--) {
        int j = rand.nextInt(i + 1);
        int[] temp = m[i];
        m[i] = m[j];
        m[j] = temp;
    }
} public static void main(String[] args) {
    int[][] m = {{1, 2}, {3, 4}, {5, 6}, {7, 8}, {9, 10}};
    System.out.println("Original matrix:");
    printMatrix(m);
    shuffle(m);
    System.out.println("Shuffled matrix:");
    printMatrix(m);
}

public static void printMatrix(int[][] m) {
    for (int i = 0; i < m.length; i++) {
        for (int j = 0; j < m[i].length; j++) {
            System.out.print(m[i][j] + " ");
        }
        System.out.println();
    }
}