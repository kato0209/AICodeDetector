





public class CurlLoggingInterceptor implements Interceptor {

    private static final Charset UTF8 = Charset.forName("UTF-8");

    private final Logger logger;
    private String curlOptions;

    public CurlLoggingInterceptor() {
        this(Logger.DEFAULT);
    }

    public CurlLoggingInterceptor(Logger logger) {
        this.logger = logger;
    }

    
    public void setCurlOptions(String curlOptions) {
        this.curlOptions = curlOptions;
    }

    @Override public Response intercept(Chain chain) throws IOException {
        Request request = chain.request();

        boolean compressed = false;

        String curlCmd = "curl";
        if (curlOptions != null) {
            curlCmd += " " + curlOptions;
        }
        curlCmd += " -X " + request.method();

        Headers headers = request.headers();
        for (int i = 0, count = headers.size(); i < count; i++) {
            String name = headers.name(i);
            String value = headers.value(i);
            if ("Accept-Encoding".equalsIgnoreCase(name) && "gzip".equalsIgnoreCase(value)) {
                compressed = true;
            }
            curlCmd += " -H " + "\"" + name + ": " + value + "\"";
        }

        RequestBody requestBody = request.body();
        if (requestBody != null) {
            Buffer buffer = new Buffer();
            requestBody.writeTo(buffer);
            Charset charset = UTF8;
            MediaType contentType = requestBody.contentType();
            if (contentType != null) {
                charset = contentType.charset(UTF8);
            }
            
            curlCmd += " --data $'" + buffer.readString(charset).replace("\n", "\\n") + "'";
        }

        curlCmd += ((compressed) ? " --compressed " : " ") + request.url();

        logger.log("╭--- cURL (" + request.url() + ")");
        logger.log(curlCmd);
        logger.log("╰--- (copy and paste the above line to a terminal)");

        return chain.proceed(request);
    }

}
