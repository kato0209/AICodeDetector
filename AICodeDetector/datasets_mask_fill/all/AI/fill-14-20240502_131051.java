import java.util.Properties;
import javax.mail.MessagingException;

public class EmailReceiver {

    public static void main(String[] args) {

       String host = "imap.example.com"; // replace with your server host
        String user = "username"; // replace with your username
       String password = "yourpassword"; // replace with your password

       Properties props = new Properties();
       props.put("mail.store.protocol", "imap");
                props.put("mail.imap.port", "993");
                try {
      