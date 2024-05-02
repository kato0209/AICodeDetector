import java.io.*;
import java.net.*;

class HttpClient {

    public static void main(String[] args) throws IOException {
        // Create a socket to connect to the server
       socket = new Socket("www.example.com", 80);

     InputStreamReader(socket.getInputStream()));  // Get input and output streams for the socket
        BufferedReader in = new BufferedReader(new request using our socket and output stream     HTTP/1.1"); PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

        // Send an HTTP InputStreamReader(in));       out.println("GET / request using our connection and output stream       out.println("Host: www.example.com");
        out.println();

  