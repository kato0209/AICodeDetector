import java.util.Scanner;

public class MaximumSquareSubmatrix {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the number of rows in the matrix: ");
        int n = input.nextInt();

        int[][] matrix = new int[n][n];
        System.out.println("Enter the elements of the matrix (0 or 1):");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = input.nextInt();
            }
        }

        int[] result = findLargestBlock(matrix);

        System.out.println("The maximum square submatrix starts at (" + result[0] + ", " + result[1] + ")");
        System.out.println("It has " + result[2] + " rows.");
    }

    public static int[] findLargestBlock(int[][] m) {
        int maxBlockSize = 0;
        int[] maxBlockLocation = new int[2];

        int n = m.length;
        int[][] dp = new int[n][n];

        // Fill the first row and column of the dp array
        for (int i = 0; i < n; i++) {
            dp[i][0] = m[i][0];
            dp[0][i] = m[0][i];
        }

        // Compute the remaining entries of the dp array
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < n; j++) {
                if (m[i][j] == 1) {
                    dp[i][j] = Math.min(dp[i-1][j-1], Math.min(dp[i-1][j], dp[i][j-1])) + 1;
                    if (dp[i][j] > maxBlockSize) {
                        maxBlockSize = dp[i][j];
                        maxBlockLocation[0] = i - maxBlockSize + 1;
                        maxBlockLocation[1] = j - maxBlockSize + 1;
                    }
                }
            }
        }

        int[] result = new int[3];
        result[0] = maxBlockLocation[0];
        result[1] = maxBlockLocation[1];
        result[2] = maxBlockSize;
        return result;
    }
}