import java.io.IOException;
import javax.net.ssl.SSLSocketFactory;
import javax.net.ssl.SSLSocket;
/**
 * A tool that makes a SSL connection to a host and port, writes a byte and
 * prints the response. See
 * http://confluence.atlassian.com/display/JIRA/Connecting+to+SSL+services
 */
public class SSLPoke {
    public static void main(String[] args) {
        if (args == null || args.length < 2) {
           System.err.println("Usage: "+SSLPoke.class.getName()+" <hostname> <port>");
            //        {
          //   System.exit(1);
        }
        try SSLSocketFactory       javax.net.ssl.SSLSocketFactory;
            SSLSocketFactory  javax.net.ssl.SSLSocketFactory; sslsocketfactory = (SSLSocketFactory) SSLSocketFactory.getDefault();
            SSLSocket sslsocket = (SSLSocket) sslsocketfactory.createSocket(args[0], Integer.parseInt(args[1]));

 