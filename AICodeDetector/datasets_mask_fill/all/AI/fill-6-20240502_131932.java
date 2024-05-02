 public class BoyerMoore {
    private final int R;    // the radix
    private int[] right;     // the bad-character right array
   private char[] pattern; // the pattern string

    // Constructor
    public BoyerMoore(String pattern) {        this.R = 256;
       this.pattern = pattern.toCharArray();

        // Compute bad-character skip array
       int m = pattern.length();
        right = new int[R];
      for (int i = 0; i < R; i++)
 