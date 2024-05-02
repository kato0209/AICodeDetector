import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class <extra_id_0>    public static void main(String[] args) {
        try {
      <extra_id_1>     ServerSocket server = <extra_id_2>        <extra_id_3>   System.out.println("FTP server started");
   <extra_id_4>        while (true) {
    <extra_id_5>   <extra_id_6>       Socket client = server.accept();
    <extra_id_7>           System.out.println("Client connected");
 <extra_id_8>              Scanner in = new Scanner(client.getInputStream());
  