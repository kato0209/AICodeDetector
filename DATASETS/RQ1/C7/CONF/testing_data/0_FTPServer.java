
public class FTPServerExample {
    public static void main(String[] args) {
        try {
            ServerSocket server = new ServerSocket(21);
            System.out.println("FTP server started");
            while (true) {
                Socket client = server.accept();
                System.out.println("Client connected");
                Scanner in = new Scanner(client.getInputStream());
                String command = in.nextLine();
                if (command.startsWith("RETR")) {
                    
                } else if (command.startsWith("STOR")) {
                    
                }
                in.close();
                client.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

