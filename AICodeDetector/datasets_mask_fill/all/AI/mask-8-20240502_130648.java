import java.io.*;
import java.util.zip.*;

public class Main {
    public static void <extra_id_0> {
 <extra_id_1>      // The file to compress
     <extra_id_2>  <extra_id_3> = "file.txt";
        // The compressed file
        String compressedFile = "file.zip";

    <extra_id_4>  <extra_id_5> (FileInputStream fis = new FileInputStream(fileToCompress);
         <extra_id_6>   FileOutputStream fos = new FileOutputStream(compressedFile);
           <extra_id_7> ZipOutputStream zos = new ZipOutputStream(fos)) {

          <extra_id_8> // Create a new zip entry
   