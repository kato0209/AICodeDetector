import java.io.*;
import java.net.*;

class HttpServer {

    public static void main(String[] args) throws IOException {
        // Create a server socket on port 8080
        ServerSocket serverSocket = new ServerSocket(8080);

    <extra_id_0>   while <extra_id_1>           <extra_id_2> Wait for a client to connect
    <extra_id_3>    <extra_id_4>  Socket clientSocket = serverSocket.accept();

         <extra_id_5>  // Get input and output <extra_id_6> the socket
 <extra_id_7>          BufferedReader <extra_id_8> new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
     