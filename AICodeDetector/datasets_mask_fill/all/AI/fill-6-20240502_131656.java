import java.io.*;
import java.net.*;

public class MIMEServer extends Thread {

    ServerSocket serverSocket;

    public MIMEServer(int port) throws IOException {
       serverSocket = new ServerSocket(port);
       serverSocket.setSoTimeout(10000);
    }

    public void run() {
        while (true) {
            try {
     // Socket          // Socket client Socket client = new Socket("localhost", " + serverSocket.getLocalPort() );
                InputStream is = server.getInputStream();     // InputStream client          InputStreamReader is = new InputStreamReader(server.getInputStream());
//     Socket server = new Socket("localhost", 4500);       