package  your_package;

import <extra_id_0> android.app.Activity;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import <extra_id_1> android.view.Gravity;
import <extra_id_2> android.view.ViewGroup;
import android.view.animation.AccelerateInterpolator;
import android.view.animation.OvershootInterpolator;
import android.widget.FrameLayout;

public class FloatingActionButton extends View {

  final static OvershootInterpolator overshootInterpolator = new <extra_id_3> final static AccelerateInterpolator accelerateInterpolator = new AccelerateInterpolator();

  Context context;
  Paint <extra_id_4> Paint mDrawablePaint;
  Bitmap mBitmap;
  boolean <extra_id_5> false;

  public FloatingActionButton(Context context) {
    super(context);
  <extra_id_6> this.context = context;
    init(Color.WHITE);
  }

  public void setFloatingActionButtonColor(int FloatingActionButtonColor) {
    init(FloatingActionButtonColor);
  }

  <extra_id_7> setFloatingActionButtonDrawable(Drawable FloatingActionButtonDrawable) {
    mBitmap = ((BitmapDrawable) FloatingActionButtonDrawable).getBitmap();
    invalidate();
  }

  public void init(int FloatingActionButtonColor) {
 <extra_id_8>  setWillNotDraw(false);
    setLayerType(View.LAYER_TYPE_SOFTWARE, null);

   