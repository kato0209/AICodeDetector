import java.io.File;

public class GetAllFilesAndFolders {   public static void main(String[] args) {
        String directoryPath = "C:/example/directory";
       File directory = new File(directoryPath);

       if (!directory.exists()) {
      System.out.println("The     directory does not exist.");
            return;
       }

       if (!directory.isDirectory()) {
            System.out.println("The path specified is not a directory.");
      {     return;
     