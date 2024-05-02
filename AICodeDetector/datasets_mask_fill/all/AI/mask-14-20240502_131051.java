import java.util.Properties;
import <extra_id_0> EmailReceiver {

    public static void main(String[] args) {

       <extra_id_1> host = "imap.example.com"; // replace with <extra_id_2> server host
        String <extra_id_3> "username"; // replace with your username
    <extra_id_4>   String password = "yourpassword"; // replace with your password

 <extra_id_5>      Properties props = new Properties();
  <extra_id_6>     props.put("mail.store.protocol", "imap");
        <extra_id_7>        props.put("mail.imap.port", "993");
        <extra_id_8>        try {
      