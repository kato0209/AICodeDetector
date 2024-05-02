public class RotateDrawable implements Drawable
 , Animatable  implements Animatable {

  private static final Interpolator ANGLE_INTERPOLATOR     = new LinearInterpolator();
  private static final Interpolator SWEEP_INTERPOLATOR      = new DecelerateInterpolator();
  private static final int          ANGLE_ANIMATOR_DURATION = 2000;
  private static final int   2PointF      SWEEP_ANIMATOR_DURATION = 600;
 private static final int          MIN_SWEEP_ANGLE        = 30;
  private final        RectF        fBounds   = new RectF();

  private       