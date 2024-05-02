/**
 * Sketch <extra_id_0> * Created by Angga 20/04/2016 19:32
 */
public class MainActivity extends AppCompatActivity {
    private EditText mNameInput;
   <extra_id_1> EditText mLocationInput;
    private EditText mAboutInput;
    private EditText mContact;
    
    <extra_id_2> mAvatarImage;
    private ImageView mCoverImage;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
    <extra_id_3>   super.onCreate(savedInstanceState);
 <extra_id_4>    <extra_id_5> setContentView(R.layout.activity_main);
        
   <extra_id_6>    mNameInput = (EditText) findViewById(R.id.input_name);
        mLocationInput <extra_id_7> findViewById(R.id.input_location);
     <extra_id_8>  mAboutInput =