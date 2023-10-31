public class ConnectFourGame {  private static final String RED = "R";  private static final String YELLOW = "Y";  private static final String WIN = "win";  private static final String CONTINUE = "continue";  private static final String DRAW = "draw";  private static final String EMPTY = " ";  private static final String DASH = "-";  private static final String SEP = "|";  static boolean turn = true;   public static void main(String[] args) {    int numMoves = 0;    String[][] board = new String[6][7];    for (String[] strings : board) {      Arrays.fill(strings, EMPTY);    }    Scanner in = new Scanner(System.in);    String result = CONTINUE;     while (true) {      turn = !turn;       int move = printBoard(board, turn ? YELLOW : RED, in);      playerMove(move, board, turn ? YELLOW : RED);      result = evaluateGame(board);      if (result.equals(WIN)) {        printBoard(board);        if (turn) {           System.out.println("The yellow player won.");        } else {           System.out.println("The red player won.");        }        break;      } else if (result.equals(DRAW)) {        System.out.println("The game is a draw.");      }    }  }  static void playerMove(int column, String[][] board, String player) {    for (int r = (board.length - 1); r >= 0; r--) {      String val = board[r][column];      if (val.equals(EMPTY)) {        board[r][column] = player;        break;      }    }  }  static String evaluateGame(String[][] board) {    int redPoints;    int yellowPoints = 0;        for (int r = 0; r < board.length; r++) {      redPoints = 0;      yellowPoints = 0;      for (int c = 0; c < board[r].length; c++) {        String g = board[r][c];        if (!g.equals(EMPTY)) {          if (g.equals(RED)) {            redPoints++;            yellowPoints = 0;          } else if (g.equals(YELLOW)) {            yellowPoints++;            redPoints = 0;          }          if (redPoints >= 4) {            return WIN;          } else if (yellowPoints >= 4) {            return WIN;          }        } else {          redPoints = 0;          yellowPoints = 0;        }      }    }        for (int c = 0; c < board[0].length; c++) {      redPoints = 0;      yellowPoints = 0;      for (int r = 0; r < board.length; r++) {        String g = board[r][c];        if (!g.equals(EMPTY)) {          if (g.equals(RED)) {            redPoints++;            yellowPoints = 0;          } else if (g.equals(YELLOW)) {            yellowPoints++;            redPoints = 0;          }          if (redPoints >= 4) {            return WIN;          }          if (yellowPoints >= 4) {            return WIN;          }        } else {          redPoints = 0;          yellowPoints = 0;        }      }    }        for (int r = 0; r < board.length; r++) {      for (int c = 0; c < board[r].length; c++) {        String g = board[r][c];        if (!g.equals(EMPTY)) {          if (g.equals(RED)) {            redPoints = 1;                        for (int d = 1; (r + d) < board.length && (c + d) < board[r].length; d++) {              if (board[r + d][c + d].equals(RED)) {                redPoints++;              } else {                break;              }              if (redPoints == 4) {                return WIN;              }            }            redPoints = 1;                        for (int d = 1; (r - d) >= 0 && (c + d) < board[r].length; d++) {              if (board[r - d][c + d].equals(RED)) {                redPoints++;              } else {                break;              }              if (redPoints == 4) {                return WIN;              }            }            redPoints = 1;                        for (int d = 1; (r + d) < board.length && (c - d) >= 0; d++) {              if (board[r + d][c - d].equals(RED)) {                redPoints++;              } else {                break;              }              if (redPoints == 4) {                return WIN;              }            }            redPoints = 1;                        for (int d = 1; (r - d) >= 0 && (c - d) >= 0; d++) {              if (board[r - d][c - d].equals(RED)) {                redPoints++;              } else {                break;              }              if (redPoints == 4) {                return WIN;              }            }          } else if (g.equals(YELLOW)) {            yellowPoints = 1;                        for (int d = 1; (r + d) < board.length && (c + d) < board[r].length; d++) {              if (board[r + d][c + d].equals(YELLOW)) {                yellowPoints++;              } else {                break;              }              if (yellowPoints == 4) {                return WIN;              }            }            yellowPoints = 1;                        for (int d = 1; (r - d) >= 0 && (c + d) < board[r].length; d++) {              if (board[r - d][c + d].equals(YELLOW)) {                yellowPoints++;              } else {                break;              }              if (yellowPoints == 4) {                return WIN;              }            }            yellowPoints = 1;                        for (int d = 1; (r + d) < board.length && (c - d) >= 0; d++) {              if (board[r + d][c - d].equals(YELLOW)) {                yellowPoints++;              } else {                break;              }              if (yellowPoints == 4) {                return WIN;              }            }            yellowPoints = 1;                        for (int d = 1; (r - d) >= 0 && (c - d) >= 0; d++) {              if (board[r - d][c - d].equals(YELLOW)) {                yellowPoints++;              } else {                break;              }              if (yellowPoints == 4) {                return WIN;              }            }          }        }      }    }    return CONTINUE;  }  static int printBoard(String[][] board, String player, Scanner in) {    printBoard(board);    System.out.print("Drop a " + (player.equals(RED) ? "red" : "yellow") + " disk at column (0" + DASH + "6): ");    int move = in.nextInt();    return move;  }  static void printBoard(String[][] board) {    for (String[] strings : board) {      for (String s : strings) {        System.out.print(SEP + s);      }      System.out.println(SEP);    }    System.out.println(DASH + DASH + DASH + DASH + DASH + DASH + DASH + DASH + DASH + DASH + DASH + DASH + DASH + DASH + DASH);  }}