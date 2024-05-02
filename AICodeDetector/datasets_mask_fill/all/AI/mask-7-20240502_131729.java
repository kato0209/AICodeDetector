import java.util.*;
import javax.mail.*;
import javax.mail.internet.*;

public class EmailSender {

    public static <extra_id_0> args) {

        String to = "recipient@example.com"; // replace with recipient email address
        <extra_id_1> = "sender@example.com"; // replace with sender email address
  <extra_id_2>     String password = "yourpassword"; // replace with sender email password

        Properties props = new Properties();
  <extra_id_3>   <extra_id_4> props.put("mail.smtp.host", "smtp.gmail.com"); // replace <extra_id_5> server of your email provider
 <extra_id_6>      <extra_id_7> // replace with port number of SMTP server
        props.put("mail.smtp.auth", <extra_id_8>    