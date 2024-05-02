<extra_id_0> javax.swing.JFrame;
import javax.swing.JTextField;

public class MatrixDisplay {
    public static void main(String[] args) {
  <extra_id_1>     JFrame frame = <extra_id_2> Display");
      <extra_id_3> frame.setSize(500, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

       <extra_id_4> matrix = new int[10][10];
 <extra_id_5>   <extra_id_6>  Random rand = new Random();

    <extra_id_7>   for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
          <extra_id_8>     matrix[i][j] = rand.nextInt(2); // generate