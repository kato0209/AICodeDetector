import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

public class Main {
    public static void main(String[] args) {
   <extra_id_0>   <extra_id_1> {
 <extra_id_2>          // Get file
            File file = new File("example.txt");
        <extra_id_3>    <extra_id_4>      // Read <extra_id_5> byte <extra_id_6>         <extra_id_7> byte[] fileContent = Files.readAllBytes(file.toPath());
        
           <extra_id_8> Print the byte array
         