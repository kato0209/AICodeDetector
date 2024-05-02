import java.io.*;
import java.net.*;

public class ChatClient {
    private static BufferedReader in;
    private static PrintWriter out;

    public static void main(String[] args) throws IOException {
        Socket socket = null;
        try {
            socket = new Socket("localhost", 8080);
            in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));

            String input;
            while ((input = stdIn.readLine()) != null) {
                out.println(input);
                String response = in.readLine();
                if (response != null) {
                    System.out.println(response);
                }
            }
        } catch (UnknownHostException e) {
            System.err.println("Unknown host: localhost");
            System.exit(-1);
        } catch (IOException e) {
            System.err.println("Error connecting to server");
            System.exit(-1);
        } finally {
            if (socket != null) {
                socket.close();
            }
        }
    }
}

