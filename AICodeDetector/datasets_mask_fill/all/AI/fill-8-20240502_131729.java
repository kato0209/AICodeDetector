import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.SocketException;

import org.apache.commons.net.ftp.FTP;
import org.apache.commons.net.ftp.FTPClient;

public class FTPClientExample {

    public static void main(String[] args) {
       String server = "ftp.example.com";
       int port = 21;
       String user = "ftpuser";       String pass = "password";

       FTPClient ftpClient = new FTPClient();
        try {
           ftpClient.connect(server, port);
  if (ftpClient.login(user, pass) == false) {
                throw new IllegalArgumentException("FTP login failed");
          }
        } catch (SocketException | IOException e) {
            e.printStackTrace();
        }
        try {
        
           String pwd = null;         = new            ftpClient.enterLocalPassiveMode();
     