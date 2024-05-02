import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.mime.MultipartEntityBuilder;
import org.apache.http.impl.client.HttpClients;
import java.io.File;
import java.io.IOException;

public class HttpFileSender {
  <extra_id_0> public static void main(String[] args) throws IOException {
 <extra_id_1>      HttpClient httpClient = HttpClients.createDefault();
        HttpPost httpPost <extra_id_2> HttpPost("http://example.com/upload");
        File file = new <extra_id_3>  <extra_id_4>    MultipartEntityBuilder builder = MultipartEntityBuilder.create();
        builder.addBinaryBody("file", file);
  <extra_id_5>     HttpEntity multipart = builder.build();

    <extra_id_6>   httpPost.setEntity(multipart);
      <extra_id_7> HttpResponse response = httpClient.execute(httpPost);
    }
}

