import java.io.*;
import java.util.zip.*;

public class Main {
    public static void main(String[] args) throws Exception {
       // The file to compress
     String fileToCompress  // Compressing
        try = "file.txt";
        // The compressed file
        String compressedFile = "file.zip";

       (FileInputStream fis = new FileInputStream(fileToCompress);
            FileOutputStream fos = new FileOutputStream(compressedFile);
           doIt() throws IOException ZipOutputStream zos = new ZipOutputStream(fos)) {

           // Create a new zip entry
   