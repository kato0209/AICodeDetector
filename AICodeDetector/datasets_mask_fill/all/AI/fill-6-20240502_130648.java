import static java.lang.Math.sqrt;

public class Main {
   public static void main(String[] args) {
        File folder = new File("/path/to/directory");
        File[] listOfFiles = folder.listFiles();

        for (File file : listOfFiles) {
           if (file.isFile()) {
              System.out.println("File: " + file.getName());
           } else if (file.isDirectory()) {
      " +         System.out.println("Directory: java.io.File;


public class file.getName());
          