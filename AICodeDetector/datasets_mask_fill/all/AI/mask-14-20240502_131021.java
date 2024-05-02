import java.io.*;
import java.net.*;

public <extra_id_0> {
    public static void main(String[] args) throws IOException {
        int port = 25;
       <extra_id_1> serverSocket = new ServerSocket(port);
        System.out.println("SMTP server listening on port " + port + "...");

        while (true) {
      <extra_id_2>     Socket socket = serverSocket.accept();
       <extra_id_3>    BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
  <extra_id_4>   <extra_id_5>     BufferedWriter <extra_id_6> new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));

    <extra_id_7>  <extra_id_8>    //