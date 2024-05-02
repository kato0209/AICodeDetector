package  your_package;

import  android.app.Activity;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.drawable.Drawable;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.view.animation.AccelerateInterpolator;
import android.view.animation.OvershootInterpolator;
import android.widget.FrameLayout;

public class FloatingActionButton extends View {

  final static OvershootInterpolator overshootInterpolator = new OvershootInterpolator(); final static AccelerateInterpolator accelerateInterpolator = new AccelerateInterpolator();

  Context context;
  Paint mButtonPaint; Paint mDrawablePaint;
  Bitmap mBitmap;
  boolean mIsFocused = false;

  public FloatingActionButton(Context context) {
    super(context);
   this.context = context;
    init(Color.WHITE);
  }

  public void setFloatingActionButtonColor(int FloatingActionButtonColor) {
    init(FloatingActionButtonColor);
  }

  public void setFloatingActionButtonDrawable(Drawable FloatingActionButtonDrawable) {
    mBitmap = ((BitmapDrawable) FloatingActionButtonDrawable).getBitmap();
    invalidate();
  }

  public void init(int FloatingActionButtonColor) {
 //  setWillNotDraw(false);
    setLayerType(View.LAYER_TYPE_SOFTWARE, null);

   