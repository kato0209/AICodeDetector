import java.io.File;

public class GetAllFilesAndFolders <extra_id_0>   public static void main(String[] args) {
        String directoryPath = "C:/example/directory";
     <extra_id_1>  File <extra_id_2> new File(directoryPath);

 <extra_id_3>      if (!directory.exists()) {
      <extra_id_4>    <extra_id_5> directory does not exist.");
            return;
   <extra_id_6>    }

      <extra_id_7> if (!directory.isDirectory()) {
            System.out.println("The path specified is not a directory.");
      <extra_id_8>     return;
     