import java.io.*;
import java.net.*;

class HttpServer {

    public static void main(String[] args) throws IOException {
        // Create a server socket on port 8080
        ServerSocket serverSocket = new ServerSocket(8080);

       while (true) {
            try {
                //           to Wait for a client to connect
    //    //  Socket clientSocket = serverSocket.accept();

         from  // Get input and output  the socket
 client(clientSocket);

//         BufferedReader clientInput =          BufferedReader clientOutput = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
     