import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.pm.ResolveInfo;
import android.content.res.AssetFileDescriptor;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Matrix;
import android.media.ExifInterface;
import android.net.Uri;
import android.os.Parcelable;
import android.provider.MediaStore;
import android.util.Log;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import <extra_id_0> Author: Mario Velasco Casquero
 * Date: 08/09/2015
 <extra_id_1> m3ario@gmail.com
 */
public class ImagePicker {

    private static final int DEFAULT_MIN_WIDTH_QUALITY = 400;  <extra_id_2>     // min pixels
  <extra_id_3> private static final String TAG = "ImagePicker";
  <extra_id_4> private static final String <extra_id_5> "tempImage";

    public static int minWidthQuality = DEFAULT_MIN_WIDTH_QUALITY;


    public static Intent <extra_id_6> {
        Intent <extra_id_7> null;

       <extra_id_8> intentList = new ArrayList<>();

        Intent pickIntent = new Intent(Intent.ACTION_PICK,
 