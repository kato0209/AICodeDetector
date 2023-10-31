import java.io.File;
import java.text.SimpleDateFormat;

public class Main {
    public static void main(String[] args) {
        
        File file = new File("example.txt");
    
        
        long lastModified = file.lastModified();
    
        
        SimpleDateFormat sdf = new SimpleDateFormat("MM/dd/yyyy HH:mm:ss");
    
        
        System.out.println("Last modified: " + sdf.format(lastModified));
    }
}

