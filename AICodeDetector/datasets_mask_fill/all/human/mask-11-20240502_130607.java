import javax.net.ssl.HttpsURLConnection;
import java.awt.Color;
import java.io.IOException;
import java.io.OutputStream;
import java.lang.reflect.Array;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Class used to execute Discord Webhooks with <extra_id_0> */
public class DiscordWebhook <extra_id_1>   private final <extra_id_2>    <extra_id_3> content;
    private String username;
    private String avatarUrl;
    private boolean tts;
    private List<EmbedObject> <extra_id_4> new ArrayList<>();

    /**
     * Constructs a new DiscordWebhook instance
   <extra_id_5> *
     * @param url The webhook URL obtained in Discord
   <extra_id_6> */
    public DiscordWebhook(String url) {
     <extra_id_7>  this.url = url;
  <extra_id_8> }

    public