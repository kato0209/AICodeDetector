<extra_id_0> com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.ParseError;
import com.android.volley.Request;
import <extra_id_1> com.android.volley.toolbox.HttpHeaderParser;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.Map;

/**
 * Custom request to make multipart header and upload file.
 * 
 * Sketch Project Studio
 * Created by Angga on <extra_id_2> */
public class VolleyMultipartRequest extends Request<NetworkResponse> {
  <extra_id_3> private final String twoHyphens = "--";
    private final String lineEnd = "\r\n";
    private final String boundary = "apiclient-" + <extra_id_4>   private Response.Listener<NetworkResponse> <extra_id_5>   private Response.ErrorListener mErrorListener;
    <extra_id_6> String> mHeaders;

    /**
 <extra_id_7>   <extra_id_8> constructor with predefined header and post method.
     *
     * @param url       