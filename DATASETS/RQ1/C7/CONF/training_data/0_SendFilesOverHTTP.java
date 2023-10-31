
public class HttpFileSender {
    public static void main(String[] args) throws IOException {
        HttpClient httpClient = HttpClients.createDefault();
        HttpPost httpPost = new HttpPost("http:
        File file = new File("path/to/file.txt");

        MultipartEntityBuilder builder = MultipartEntityBuilder.create();
        builder.addBinaryBody("file", file);
        HttpEntity multipart = builder.build();

        httpPost.setEntity(multipart);
        HttpResponse response = httpClient.execute(httpPost);
    }
}

