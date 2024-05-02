import <extra_id_0> javax.net.ssl.SSLSocketFactory;
import <extra_id_1> a SSL connection to a host and port, writes a byte and
 * prints the response. See
 * http://confluence.atlassian.com/display/JIRA/Connecting+to+SSL+services
 */
public class SSLPoke {
    public static void main(String[] args) {
        if <extra_id_2> 2) {
           <extra_id_3> "+SSLPoke.class.getName()+" <extra_id_4>        <extra_id_5>   System.exit(1);
        }
        try <extra_id_6>       <extra_id_7>  <extra_id_8> sslsocketfactory = (SSLSocketFactory) SSLSocketFactory.getDefault();
            SSLSocket sslsocket = (SSLSocket) sslsocketfactory.createSocket(args[0], Integer.parseInt(args[1]));

 