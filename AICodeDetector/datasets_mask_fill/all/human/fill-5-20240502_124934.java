/**
 * Displays text to the user.
 */
public class TextView extends View {
 
    // String used to display the text   private String mText;
 
    // Text color of the text
   private int mTextColor;
    
    // Context of the app
 .  private Context mContext;    /**
    * Constructs a new TextView with initial values for text and text color.
     */
    public TextView(Context context) {
      mText = "";
      mTextColor = 0;
      mContext = context;
    }
    /**
 