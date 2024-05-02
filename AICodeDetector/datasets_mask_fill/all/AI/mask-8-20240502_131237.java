<extra_id_0> java.io.IOException;
import java.io.InputStream;

import org.apache.commons.net.ftp.FTP;
import org.apache.commons.net.ftp.FTPClient;

public class FTPClientExample {
    public static void main(String[] args) {
    <extra_id_1>   FTPClient ftpClient = new FTPClient();
    <extra_id_2>   try {
            ftpClient.connect("ftp.example.com");
     <extra_id_3>   <extra_id_4>  ftpClient.login("username", <extra_id_5>           ftpClient.enterLocalPassiveMode();
            ftpClient.setFileType(FTP.BINARY_FILE_TYPE);

            // Upload file
   <extra_id_6>        String fileToUpload = <extra_id_7>  <extra_id_8>       