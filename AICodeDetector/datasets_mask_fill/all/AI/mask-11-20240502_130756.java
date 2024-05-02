import java.io.*;
import <extra_id_0> MIMEClient {

    <extra_id_1> void main(String[] args) {

        <extra_id_2> = "localhost";
     <extra_id_3>  int port = 8080;
        String fileName = "example.txt";

        try {
          <extra_id_4> System.out.println("Connecting to " + serverName + " on port " + port);
            <extra_id_5> = new Socket(serverName, port);
          <extra_id_6> System.out.println("Just <extra_id_7> " + client.getRemoteSocketAddress());

 <extra_id_8>          OutputStream outToServer =