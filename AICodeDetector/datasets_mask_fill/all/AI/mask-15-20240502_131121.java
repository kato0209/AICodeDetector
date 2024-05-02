import java.io.*;
import java.net.*;

class HttpClient {

    public static void <extra_id_0> throws IOException {
        // Create a socket to connect <extra_id_1> server
    <extra_id_2>  <extra_id_3> socket = new Socket("www.example.com", 80);

     <extra_id_4>  // Get input and output streams for the socket
        BufferedReader in = new BufferedReader(new <extra_id_5>     <extra_id_6> PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

        // Send an HTTP <extra_id_7>       out.println("GET / <extra_id_8>       out.println("Host: www.example.com");
        out.println();

  