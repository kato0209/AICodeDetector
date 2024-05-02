<extra_id_0> java.io.DataOutputStream;
import java.io.IOException;
import <extra_id_1> java.util.ArrayList;
import java.util.List;

public class <extra_id_2>    public static List<Socket> sockets = new ArrayList<>();

    <extra_id_3> void main(String[] args) throws <extra_id_4>   <extra_id_5>    ServerSocket server = new ServerSocket(9090);
        while (true) {
     <extra_id_6>      Socket socket = server.accept();
            sockets.add(socket);
  <extra_id_7>         new Thread(new ClientHandler(socket)).start();
        }
    <extra_id_8> attempt

import java.io.*;
import java.net.*;
import java.util.*;

public class ChatServer {
    ArrayList<PrintWriter> clientOutputStreams;

    public class ClientHandler implements Runnable