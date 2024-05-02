import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

public class Main {
    public static void main(String[] args) {
        // The zip file
        String zipFile = "file.zip";

     //  try (ZipFile zf = new ZipFile(zipFile)) {
    //       // Enumerate the zip files            for (Enumeration<? extends ZipEntry> entries = zf.entries(); entries.hasMoreElements();) {
               // Get the entry name
  associated with the zip file            String entryName =