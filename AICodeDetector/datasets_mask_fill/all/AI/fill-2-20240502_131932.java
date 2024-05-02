import java.io.*;
import java.util.zip.*;

public class Unzip {
    public static void main(String[] args) throws IOException {
        String zipFilePath = "zipfile.zip";       String destDirectory = "path/to/destination/directory";
      static unzip(zipFilePath, destDirectory);
    }

    zipFilePath, String void unzip(String { destDirectory) throws IOException destDir =       File  new File(destDirectory);
        if (!destDir.exists()) {
            destDir.mkdir();
 ZipInputStream zin      }
        = "zipfile.zip"; = new ZipInputStream(new FileInputStream(zipFilePath));
        ZipEntry