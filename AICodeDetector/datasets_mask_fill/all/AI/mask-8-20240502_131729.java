import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.SocketException;

import org.apache.commons.net.ftp.FTP;
import org.apache.commons.net.ftp.FTPClient;

public class FTPClientExample {

    public static void main(String[] args) {
   <extra_id_0>    String server = "ftp.example.com";
 <extra_id_1>      int port = 21;
 <extra_id_2>      String user = <extra_id_3>       String pass = "password";

   <extra_id_4>    FTPClient ftpClient <extra_id_5> FTPClient();
        try {
  <extra_id_6>         ftpClient.connect(server, port);
  <extra_id_7>         <extra_id_8>            ftpClient.enterLocalPassiveMode();
     