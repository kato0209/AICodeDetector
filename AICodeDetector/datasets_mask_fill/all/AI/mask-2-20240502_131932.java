import java.io.*;
import java.util.zip.*;

public class Unzip {
    public static void main(String[] args) throws IOException {
        String zipFilePath <extra_id_0>  <extra_id_1>     String destDirectory = "path/to/destination/directory";
      <extra_id_2> unzip(zipFilePath, destDirectory);
    }

    <extra_id_3> void unzip(String <extra_id_4> destDirectory) throws IOException <extra_id_5>       File <extra_id_6> new File(destDirectory);
        if (!destDir.exists()) {
            destDir.mkdir();
 <extra_id_7>      }
        <extra_id_8> = new ZipInputStream(new FileInputStream(zipFilePath));
        ZipEntry