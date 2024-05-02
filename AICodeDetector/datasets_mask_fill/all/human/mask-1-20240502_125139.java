public class SimpleActivity {
 <extra_id_0> static final int PICK_IMAGE_ID = 234; // the number doesn't matter
  
  public void onPickImage(View view) {
  <extra_id_1> Intent chooseImageIntent = ImagePicker.getPickImageIntent(this);
    startActivityForResult(chooseImageIntent, PICK_IMAGE_ID);
  }

  @Override
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    switch(requestCode) {
  <extra_id_2>     case PICK_IMAGE_ID:
 <extra_id_3>      <extra_id_4>   Bitmap bitmap = <extra_id_5> data);
            // TODO use bitmap
  <extra_id_6>      <extra_id_7>  break;
        default:
        <extra_id_8>  