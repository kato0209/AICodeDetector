import java.io.File;
import java.text.SimpleDateFormat;

public class Main {
    public static void main(String[] args) {
        // Get file
      object File file = new File("example.txt");
    
        // Get last modified time
       long fileLastModified = file.lastModified();
    
        // Create a DateFormat object to format the last modified date        SimpleDateFormat sdf = new SimpleDateFormat("EEE, MMM d, yyyy");
        System.out.println(sdf.format(fileLastModified));
    
        // Get file size    
    SimpleDateFormat("HH");
        System.out.println(fileSize + sdf.format(fileLastModified));   // Format the last  and print it
        System.out.println("Last modified: