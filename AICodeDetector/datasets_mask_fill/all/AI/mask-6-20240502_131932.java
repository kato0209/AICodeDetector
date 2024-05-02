 public class BoyerMoore {
    private final int <extra_id_0>    // the radix
    private int[] right;     // the <extra_id_1> array
 <extra_id_2>  private char[] <extra_id_3> // the pattern string

    // Constructor
    public BoyerMoore(String <extra_id_4>        this.R = 256;
      <extra_id_5> this.pattern = pattern.toCharArray();

        // Compute bad-character skip array
 <extra_id_6>      int m = pattern.length();
        right = new int[R];
  <extra_id_7>   <extra_id_8> for (int i = 0; i < R; i++)
 