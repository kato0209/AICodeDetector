import java.io.*;
import java.net.*;

public class SMTP {
    public static void main(String[] args) throws IOException {
        int port = 25;
       ServerSocket serverSocket = new ServerSocket(port);
        System.out.println("SMTP server listening on port " + port + "...");

        while (true) {
           Socket socket = serverSocket.accept();
           BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
          BufferedWriter out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));

    //
	    // The SMTP program tries to send mail. It is assumed that the stream is closed
	    // manually by the user. Also, its responsibility should not be closed after this.      //