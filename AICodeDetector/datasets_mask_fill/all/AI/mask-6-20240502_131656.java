import java.io.*;
import java.net.*;

public class MIMEServer extends Thread {

   <extra_id_0> ServerSocket serverSocket;

    public MIMEServer(int port) throws IOException {
   <extra_id_1>    serverSocket = new ServerSocket(port);
     <extra_id_2>  serverSocket.setSoTimeout(10000);
    }

    public void run() {
        while (true) {
            try {
     <extra_id_3>          <extra_id_4> client <extra_id_5> " + serverSocket.getLocalPort() <extra_id_6>          <extra_id_7>     Socket server = <extra_id_8>       