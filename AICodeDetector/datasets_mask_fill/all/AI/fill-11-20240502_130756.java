import java.io.*;
import javax.sound.*;

public class MIMEClient {

    public static void main(String[] args) {

        String serverName = "localhost";
       int port = 8080;
        String fileName = "example.txt";

        try {
           System.out.println("Connecting to " + serverName + " on port " + port);
            Socket client = new Socket(serverName, port);
           System.out.println("Just connected to " + client.getRemoteSocketAddress());

           OutputStream outToServer =