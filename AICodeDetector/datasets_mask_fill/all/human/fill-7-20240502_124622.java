package android.support.webview;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.ParseError;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.toolbox.HttpHeaderParser;

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
 * Created by Angga on 11/16/14. */
public class VolleyMultipartRequest extends Request<NetworkResponse> {
   private final String twoHyphens = "--";
    private final String lineEnd = "\r\n";
    private final String boundary = "apiclient-" + System.currentTimeMillis();   private Response.Listener<NetworkResponse> mListener;   private Response.ErrorListener mErrorListener;
    private HttpHeaders<String, String> mHeaders;

    /**
 * Default   request constructor with predefined header and post method.
     *
     * @param url       