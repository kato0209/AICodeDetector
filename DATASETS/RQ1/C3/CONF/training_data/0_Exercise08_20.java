import java.util.Scanner;

public class ConnectFour {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char[][] board = new char[6][7]; // Define the game board
        initializeBoard(board); // Initialize the board to empty spaces
        char player = 'R'; // Start with player 1 (red)
        boolean gameOver = false;

        while (!gameOver) {
            printBoard(board); // Print the current board state
            int column = getColumn(scanner, player); // Prompt the current player to choose a column
            int row = dropDisk(board, column, player); // Drop the disk in the chosen column
            if (checkWin(board, row, column)) { // Check if the player has won
                System.out.println(player + " wins!");
                gameOver = true;
            } else if (isBoardFull(board)) { // Check if the board is full (i.e. a draw)
                System.out.println("Draw!");
                gameOver = true;
            } else {
                player = switchPlayer(player); // Switch to the other player
            }
        }
    }

    // Initializes the board to empty spaces
    public static void initializeBoard(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                board[i][j] = ' ';
            }
        }
    }

    // Prints the current board state
    public static void printBoard(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                System.out.print("|" + board[i][j]);
            }
            System.out.println("|");
        }
        System.out.println("---------------");
        System.out.println(" 0 1 2 3 4 5 6");
    }

    // Prompts the current player to choose a column
    public static int getColumn(Scanner scanner, char player) {
        System.out.print("Drop a " + player + " disk at column (0-6): ");
        int column = scanner.nextInt();
        return column;
    }

    // Drops the disk in the chosen column and returns the row where it landed
    public static int dropDisk(char[][] board, int column, char player) {
        for (int i = board.length - 1; i >= 0; i--) {
            if (board[i][column] == ' ') {
                board[i][column] = player;
                return i;
            }
        }
        return -1; // Column is full
    }

    // Switches to the other player
    public static char switchPlayer(char player) {
        if (player == 'R') {
            return 'Y';
        } else {
            return 'R';
        }
    }

    // Checks if the player has won
    public static boolean checkWin(char[][] board, int row, int column) {
        char player = board[row][column];

        // Check horizontal
        int count = 0;
        for (int j = 0; j < board[0].length; j++) {
            if (board[row][j] == player) {
                count++;
                if (count == 4) {
                    return true;
                }
            } else {
                count = 0;
            }
        }

        // Check vertical
        count = 0;
        for (int i = 0; i < board.length;