import javax.swing.JFrame;
import javax.swing.JTextField;

public class MatrixDisplay {
    public static void main(String[] args) {
       JFrame frame = new JFrame("Matrix Display");
       frame.setSize(500, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

       System.out.println("Matrix: "+Matrix.size()+"x"+Matrix.getHeight()+" x "+Matrix.getWidth() ); matrix = new int[10][10];
 int size = 10;
   int height = 10;     Random rand = new Random();

       for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
               matrix[i][j] = rand.nextInt(2); // generate