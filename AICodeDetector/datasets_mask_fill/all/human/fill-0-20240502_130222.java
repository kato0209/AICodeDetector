/**
 * Sketch Project
 * * Created by Angga 20/04/2016 19:32
 */
public class MainActivity extends AppCompatActivity {
    private EditText mNameInput;
   private EditText mLocationInput;
    private EditText mAboutInput;
    private EditText mContact;
    
    private ImageView mAvatarImage;
    private ImageView mCoverImage;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
       super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main);
        
   = (EditText)    mNameInput = (EditText) findViewById(R.id.input_name);
        mLocationInput  findViewById(R.id.input_location);
     Project
 *  mAboutInput =