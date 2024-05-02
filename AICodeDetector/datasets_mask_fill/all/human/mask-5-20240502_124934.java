/**
 * Displays text to the user.
 */
public <extra_id_0> extends View {
 
    // String <extra_id_1>   private String mText;
 
    // Text color of the text
 <extra_id_2>  private int mTextColor;
    
    // Context of the app
 <extra_id_3>  private Context <extra_id_4>    /**
  <extra_id_5>  * <extra_id_6> new TextView with initial values for text <extra_id_7> color.
     */
    public TextView(Context context) {
      mText = "";
      mTextColor = 0;
      mContext = context;
    }
 <extra_id_8>   /**
 