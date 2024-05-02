import java.io.File;
import java.text.SimpleDateFormat;

public class Main {
    <extra_id_0> void main(String[] args) {
        // Get file
      <extra_id_1> File file = new File("example.txt");
    
        <extra_id_2> last modified time
      <extra_id_3> long <extra_id_4> file.lastModified();
    
        // Create a DateFormat object to format the last <extra_id_5>        SimpleDateFormat sdf = new <extra_id_6>    
    <extra_id_7>   // Format the last <extra_id_8> and print it
        System.out.println("Last modified: