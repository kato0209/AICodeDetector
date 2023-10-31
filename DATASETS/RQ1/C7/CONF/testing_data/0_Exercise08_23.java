
public class FindFlippedCell {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        
        System.out.println("Enter a 6-by-6 matrix row by row:");
        int[][] matrix = new int[6][6];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                matrix[i][j] = input.nextInt();
            }
        }

        
        int row = -1, col = -1;
        for (int i = 0; i < matrix.length; i++) {
            int rowSum = 0, colSum = 0;
            for (int j = 0; j < matrix[i].length; j++) {
                rowSum += matrix[i][j];
                colSum += matrix[j][i];
            }
            if (rowSum % 2 != 0) {
                row = i;
            }
            if (colSum % 2 != 0) {
                col = i;
            }
        }

        
        System.out.println("The flipped cell is at (" + row + ", " + col + ")");
    }
}
