import java.util.Properties;
import javax.mail.Session;
import javax.mail.Message;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class EmailClient {

    <extra_id_0> void main(String[] args) {
        try {
      <extra_id_1>     Properties props = new Properties();
        <extra_id_2>   props.put("mail.smtp.host", "smtp.example.com");
          <extra_id_3> props.put("mail.smtp.port", "587");
    <extra_id_4>       <extra_id_5>    <extra_id_6>     <extra_id_7> props.put("mail.smtp.starttls.enable", "true");

      <extra_id_8>     Session session = Session.getInstance(props, null);

            Message message = new MimeMessage(session);
