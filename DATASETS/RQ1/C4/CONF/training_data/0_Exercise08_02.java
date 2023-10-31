import java.util.Random;
import java.util.Scanner;

public class MatrixAnalyzer {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size for the matrix: ");
        int n = scanner.nextInt();

        int[][] matrix = new int[n][n];

        Random random = new Random();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = random.nextInt(2);
            }
        }

        System.out.println("The matrix is:");
        printMatrix(matrix);

        boolean allZerosOrOnes;

        
        for (int i = 0; i < n; i++) {
            allZerosOrOnes = true;
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] != matrix[i][0]) {
                    allZerosOrOnes = false;
                    break;
                }
            }
            if (allZerosOrOnes) {
                System.out.printf("All %ds on row %d\n", matrix[i][0], i + 1);
            }
        }

        
        for (int j = 0; j < n; j++) {
            allZerosOrOnes = true;
            for (int i = 1; i < n; i++) {
                if (matrix[i][j] != matrix[0][j]) {
                    allZerosOrOnes = false;
                    break;
                }
            }
            if (allZerosOrOnes) {
                System.out.printf("All %ds on column %d\n", matrix[0][j], j + 1);
            }
        }

        
        allZerosOrOnes = true;
        for (int i = 1; i < n; i++) {
            if (matrix[i][i] != matrix[0][0]) {
                allZerosOrOnes = false;
                break;
            }
        }
        if (allZerosOrOnes) {
            System.out.printf("All %ds on the major diagonal\n", matrix[0][0]);
        }

        
        allZerosOrOnes = true;
        for (int i = 1; i < n; i++) {
            if (matrix[i][n - i - 1] != matrix[0][n - 1]) {
                allZerosOrOnes = false;
                break;
            }
        }
        if (allZerosOrOnes) {
            System.out.printf("All %ds on the sub-diagonal\n", matrix[0][n - 1]);
        }
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int cell : row) {
                System.out.print(cell);
            }
            System.out.println();
        }
    }
}