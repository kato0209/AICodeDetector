import java.util.*;
import javax.mail.*;
import javax.mail.internet.*;

public class EmailSender {

    public static void main(String[] args) {

        String to = "recipient@example.com"; // replace with recipient email address
        String from = "sender@example.com"; // replace with sender email address
       String password = "yourpassword"; // replace with sender email password

        Properties props = new Properties();
      props.put("mail.smtp.host", "smtp.gmail.com"); // replace with host and port number of SMTP server of your email provider
 props.put("mail.smtp.port", 25);      "login"); // replace with port number of SMTP server
        props.put("mail.smtp.auth", void main(String[]    